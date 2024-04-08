"""This is the invocation module to initiate Training Pipeline"""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.model_selection import GridSearchCV, RepeatedStratifiedKFold, train_test_split
from sklearn.linear_model import LogisticRegression

from src.logger import get_logger, Logger
from src.config import dataset_config, hyperparams_config
from src.database.feature_store import FeatureStore
from src.model.pipeline import BucketizerParams, ClassificationEvaluation
from src.util import artifacts, evaluation, pre_process


logger: Logger = get_logger(__name__)

def _fetch_pipeline() -> Pipeline:

    """
    Predefined Pipeline configuration which consists of Feature Engineering & Model building
    """

    num_pipe = Pipeline([
        ('std_scaler', StandardScaler())
    ])

    ord_pipe = Pipeline([
        ('ord_enc', OrdinalEncoder()),
    ])

    nom_pipe = Pipeline([
        # Make OHE's sparse value as False if we're converting output to pandas DataFrame
        ('nom_enc', OneHotEncoder()),
    ])

    feat_trans = ColumnTransformer([
        ('num_trans', num_pipe, dataset_config.TRANS_NUM_FEATS),
        ('cat_ord_trans', ord_pipe, dataset_config.TRANS_ORD_FEATS),
        ('cat_nom_trans', nom_pipe, dataset_config.TRANS_NOM_FEATS)
    ])

    pipeline = Pipeline([
        # Bucket Age Feature
        ('age_bucket', pre_process.Bucketizer(BucketizerParams(
            dataset_config.RAW_COL_AGE,
            dataset_config.TRANS_COL_AGE,
            [0, 9, 19, 39, 59, 79, 100],
            ['Child', 'Adolescence', 'Young Adult', 'Middle Aged', 'Aged', '80+']
        ))),

        # Bucket Cholesterol Feature
        ('cholesterol_bucket', pre_process.Bucketizer(BucketizerParams(
            dataset_config.RAW_COL_CHOLESTEROL,
            dataset_config.TRANS_COL_CHOLESTEROL,
            [-1, 199, 239, 1000],
            labels=['Normal', 'At-Risk', 'Dangerous']
        ))),

        # Feature Transformation
        ('feat_trans', feat_trans),

        # Logistic Regression
        ('log_reg', LogisticRegression())
    ])
    # pipeline.set_output(transform='pandas')

    return pipeline

def exec_pipeline() -> None:

    """
    This function is to execute the Training pipeline
    """

    try:

        # Connect to Feature Store
        logger.info('Connect to Feature Store')
        fs = FeatureStore()

        # Load data from Feature Store
        logger.info('Load data from Feature Store')
        df: pd.DataFrame = fs.load_data_from_fs()

        logger.info('Fetching the training pipeline')
        model_pipe = _fetch_pipeline()

        logger.info('Splitting the dataset into Train & Test %s', df.columns)
        x_train, x_test, y_train, y_test = train_test_split(
            df.drop(dataset_config.RAW_COL_HEART_DISEASE, axis=1),
            df[dataset_config.RAW_COL_HEART_DISEASE],
            stratify=df[dataset_config.RAW_COL_HEART_DISEASE],
            random_state=42,
            test_size=0.2
        )

        logger.info('Configuring GridSearch with Stratified KFold CV')
        cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=42)
        clf = GridSearchCV(
            model_pipe,
            hyperparams_config.LOGISTIC_REGRESSION_HYPERPARAMS,
            cv=cv, scoring='accuracy',
            n_jobs=-1
        )

        logger.info('Executing training pipeline')
        clf.fit(x_train, y_train)

        logger.info(
            'Getting the best score - %s and its parameters %s', clf.best_score_, clf.best_params_)

        best_params = clf.best_params_
        best_model_pipe = _fetch_pipeline()

        logger.info('Executing training pipeline for the best params')
        best_model_pipe.set_params(**best_params)
        best_model_pipe.fit(x_train, y_train)

        logger.info('Evaluating the Trained model')
        clf_eval: ClassificationEvaluation = evaluation\
            .evaluate_classification_model(best_model_pipe, x_test, y_test)

        logger.info('Saving the Evaluation reports as Artifacts')
        artifacts.store_classification_artifacts(clf_eval)

        logger.info('Training pipeline execution completed')

    except Exception as ex:
        logger.exception(ex, stack_info=True)
        raise ex


if __name__ == '__main__':
    exec_pipeline()

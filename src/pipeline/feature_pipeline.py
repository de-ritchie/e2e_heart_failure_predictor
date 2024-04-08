"""This is the invocation module to initiate Feature Pipeline"""
import pandas as pd

from src.logger import get_logger
from src.config import core
from src.util import kaggle
from src.database import feature_store


logger = get_logger(__name__)

def exec_pipeline() -> None:

    """
    This function is to execute the Training pipeline
    """

    try:

        # Download dataset from source
        logger.info('Loading dataset from source')
        df: pd.DataFrame = kaggle.load_data_from_kaggle(
            core.RAW_DATA_SOURCE_PATH,
            core.RAW_DATA_DOWNLOAD_PATH,
            core.RAW_DATA_DOWNLOAD_FILE_NAME
        )
        logger.info('Loaded dataset from source')

        # Cleanse the dataset
        logger.info('Cleanse the loaded data')
        logger.info('Cleansed the loaded data')

        # Connect to Feature Store DB
        logger.info('Connect to Feature Store')
        fs = feature_store.FeatureStore()
        logger.info('Feature Store Connection Established')

        # Push the dataset to feature store
        logger.info('Load data into Feature Store')
        fs.load_data_to_fs(df)
        logger.info('Data loaded into Feature Store')

        logger.info('Feature pipeline execution completed')

    except Exception as ex:
        logger.exception('Error occurred while executing feature pipeline %s', ex, stack_info=True)
        raise ex

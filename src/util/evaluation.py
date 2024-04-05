"""This utility module used for Evaluating ML models"""

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.metrics import auc, classification_report, confusion_matrix,\
      ConfusionMatrixDisplay, precision_recall_curve, roc_curve, roc_auc_score,\
      PrecisionRecallDisplay, RocCurveDisplay

from src.model.pipeline import ClassificationEvaluation


def evaluate_classification_model(
        model: Pipeline, x: pd.DataFrame, y: pd.Series) -> ClassificationEvaluation:

    """
    Evaluate Classification Model & generate the required reports

    Paramerts:
    - model: A pipeline which consists of Pre-Processing & Model building stages
    - x: It is a DataFrame which consists of features and corresponding values
    - y: Output labes for the supplied DataFrame

    Returns:
    Custom Classification Report
    """

    pred_label = model.predict(x)
    pred_label_proba = model.predict_proba(x)

    precision, recall, _ = precision_recall_curve(y, pred_label_proba[:, 1])
    fpr, tpr, _ = roc_curve(y, pred_label_proba[:, 1])
    roc_auc = auc(fpr, tpr)

    return ClassificationEvaluation(
        classification_report(y, pred_label),
        ConfusionMatrixDisplay(confusion_matrix(y, pred_label)),
        PrecisionRecallDisplay(precision, recall),
        roc_auc_score(y, pred_label),
        RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc)
    )

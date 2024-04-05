"""This module holds the data models related to Pipeline module"""

from typing import List, Dict, Any
from dataclasses import dataclass
from sklearn.metrics import ConfusionMatrixDisplay, PrecisionRecallDisplay, RocCurveDisplay

@dataclass
class BucketizerParams:

    """
    Bucketizer Model for holding the properties required for Pre-Processing Pipeline
    """

    variable: str
    new_variable: str
    bins: List[int]
    labels: List[str]

@dataclass
class ClassificationEvaluation:

    """
    ClassificationEvaluation Model for holding the properties required for Evaluation module
    """

    classification_report: Dict[str, Any]
    confusion_matrix: ConfusionMatrixDisplay
    prec_rec_curve: PrecisionRecallDisplay
    roc_auc_score: float
    roc_auc_curve: RocCurveDisplay

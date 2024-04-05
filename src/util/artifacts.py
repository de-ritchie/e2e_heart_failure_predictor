"""This utility module related to storage of artifacts"""

from pathlib import Path
import matplotlib.pyplot as plt

from src.model.pipeline import ClassificationEvaluation
from src.config import core


def save_plot_as_image(dest: str, fname: str, fig):
    """
    Save Figure object to the specified directory
    """

    fig.savefig(f'{dest}{fname}.png')

def save_string_as_txt(dest:str, fname: str, content: str):
    """
    Save String object to the specified directory
    """

    with open(f'{dest}{fname}.txt', 'w', encoding='UTF-8') as txt_file:
        txt_file.write(str(content))

def store_classification_artifacts(clf_eval: ClassificationEvaluation):
    """
    Store the artifacts of the evaluation reports
    """

    Path(core.ARTIFACTS_PATH).mkdir(exist_ok=True)

    # Saving confusion matrix
    clf_eval.confusion_matrix.plot()
    save_plot_as_image(
        core.ARTIFACTS_PATH,
        'confusion_matrix',
        plt
    )

    # Saving classification report
    save_string_as_txt(
        core.ARTIFACTS_PATH,
        'classification_report',
        clf_eval.classification_report
    )

    # Saving Precision Recall curve
    clf_eval.prec_rec_curve.plot()
    save_plot_as_image(
        core.ARTIFACTS_PATH,
        'precision_recall_curve',
        plt
    )

    # Saving ROC AUC score
    save_string_as_txt(
        core.ARTIFACTS_PATH,
        'roc_auc_score',
        clf_eval.roc_auc_score
    )

    # Saving ROC AUC curve
    clf_eval.roc_auc_curve.plot()
    save_plot_as_image(
        core.ARTIFACTS_PATH,
        'roc_auc_curve',
        plt
    )

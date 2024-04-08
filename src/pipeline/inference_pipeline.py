"""This is the invocation module to initiate Inference Pipeline"""
import pandas as pd

from src.logger import get_logger


logger = get_logger(__name__)

def exec_pipeline() -> None:

    """
    This function is to execute the Inference pipeline
    """

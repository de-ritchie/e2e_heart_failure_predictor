"""This utility module used for Pre-processing dataset"""
from typing import Dict
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from src.model.pipeline import BucketizerParams

class Bucketizer(BaseEstimator, TransformerMixin):

    """
    Custom Transformer used to bucketize or create bins on a numerical feature
    """

    def __init__(self, bucketizer_params: BucketizerParams) -> None:
        self.bucketizer_params = bucketizer_params

    def fit(self, x, y=None):

        """
        Override method of TransformerMixin
        """
        return self

    def transform(self, x):

        """
        Override method of TransformerMixin
        """

        x[self.bucketizer_params.new_variable] = pd.cut(
            x[self.bucketizer_params.variable],
            bins=self.bucketizer_params.bins,
            labels=self.bucketizer_params.labels
        )
        return x

    def get_feature_names_out(self):

        """
        Override method to avoid issue when making the Transormation pipeline output as Pandas
        """
        pass

class LabelNumerizer(BaseEstimator, TransformerMixin):

    """
    Custom Transformer used to bucketize or create bins on a numerical feature
    """

    def __init__(self, col: str, mapper: Dict[str, int]) -> None:
        self.col: str = col
        self.mapper: Dict[str, int] = mapper

    def fit(self, x, y=None):
        """
        Override method of TransformerMixin
        """
        return self

    def transform(self, x: pd.DataFrame):
        """
        Override method of TransformerMixin
        """
        x = x[self.col].map(self.mapper)
        return x

    def get_feature_names_out(self):
        """
        Override method to avoid issue when making the Transormation pipeline output as Pandas
        """
        pass

"""This module holds Feature Store Functions"""
import pandas as pd
from pymongo.collection import Collection

from src.logger import get_logger
from src.config.core import FEAT_STORE_COL_NAME
from src.model.exception import FeatureStoreException
from src.database import db


logger = get_logger(__name__)

class FeatureStore:

    """Feature Store Template, where data is loaded into/read from Feature Store"""

    def __init__(self) -> None:
        self.collection: Collection = db.get_db()\
            .get_collection(FEAT_STORE_COL_NAME)

    def load_data_to_fs(self, df: pd.DataFrame) -> None:

        """
        Load the DataFrame into Feature Store collection
        
        Paramerts:
        - df: Dataset in DataFrame format
        - collection: Load data into the MongoDB Collection

        Returns:
        None
        """

        try:
            logger.info('Drop collection if exists')
            self.collection.drop()

            logger.info('Insert dataframe into the feature store collection')
            data = df.reset_index().to_dict('records')
            self.collection.insert_many(data)

        except Exception as ex:
            logger.exception(
                'Error occurred while loading data to feature store %s', ex, stack_info=True)
            raise FeatureStoreException(
                'Error occurred while loading data into feature store') from ex

    def load_data_from_fs(self) -> pd.DataFrame:

        """
        Load the from Feature Store collection

        Returns:
        Dataset in DataFrame format
        """

        try:
            docs = self.collection.find()
            df = pd.DataFrame(docs)

            return df

        except Exception as ex:
            logger.exception(
                'Error occurred while loading data from feature store %s', ex, stack_info=True)
            raise FeatureStoreException(
                'Error occurred while loading data from feature store') from ex

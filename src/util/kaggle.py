"""This utility module used for Loading dataset from Kaggle"""
from pathlib import Path
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

from src.logger import get_logger


logger = get_logger(__name__)

def load_data_from_kaggle(dataset_name: str, dest_path: str, fname: str) -> pd.DataFrame:

    """
    Load Data from Kaggle Data Source

    Parameters:
    - dataset_path: Source dataset name in the Kaggle Dataset
    - dest_path: Location of where to download the dataset
    - fname: Downloaded dataset filename

    Return:
    Dataset in DataFrame format
    """

    try:
        logger.info('Checking the presence of download destination directory')
        Path(dest_path).mkdir(exist_ok=True)

        logger.info('Authenticating Kaggle API')
        api = KaggleApi()
        api.authenticate()

        logger.info('Downloading Kaggle Dataset & Unzipping...')
        api.dataset_download_files(dataset_name, dest_path, unzip=True)

        logger.info('Reading the dataset')
        df = pd.read_csv(f'{dest_path}/{fname}')

        return df
    except Exception as ex:
        logger.exception('Error occurred while downloading dataset %s', ex, stack_info=True)
        raise ex

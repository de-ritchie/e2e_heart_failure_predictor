"""This module is related to core configurations"""
import os


LOGS_PATH = 'logs/'
ARTIFACTS_PATH='artifacts/'

# MongoDB
MONGO_DB_CONNECTION_STRING = os.environ['MONGO_DB_CONNECTION_STRING']
MONGO_DB_NAME = os.environ['MONGO_DB_NAME']

# RAW_DATA
RAW_DATA_SOURCE_PATH = 'fedesoriano/heart-failure-prediction'
RAW_DATA_DOWNLOAD_PATH = 'data'
RAW_DATA_DOWNLOAD_FILE_NAME = 'heart.csv'

# Feature Store
FEAT_STORE_COL_NAME = os.environ['FEAT_STORE_COL_NAME']

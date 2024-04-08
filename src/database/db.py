"""This module establishes Database connection"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.database import Database

from src.logger import get_logger
from src.config import core
from src.model.exception import DatabaseException


logger = get_logger(__name__)

def get_db() -> Database:
    """
    This function establises the connection to Feature Store & returns collection object
    """

    # Create a new client and connect to the server
    client = MongoClient(core.MONGO_DB_CONNECTION_STRING, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        logger.info("Successfully connected to MongoDB!")
    except Exception as ex:
        logger.exception(
            'Exception occurred while establishing connection with MongoDB %s', ex, stack_info=True)
        raise DatabaseException(
            'Exception occurred while establishing connection with MongoDB') from ex

    db: Database = client[core.MONGO_DB_NAME]
    return db

"""This module is used to setup the logger"""
import os
import zipfile
from pathlib import Path
import logging
from logging import Logger
from logging.handlers import TimedRotatingFileHandler

from src.config import core


def zipper(src, dest) -> None:

    """
    Used to handle the old log file so that it is zipped
    """

    zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED).write(
        src, os.path.basename(src)
    )
    os.remove(src)

def get_logger(name: str) -> Logger:

    """Setting up Logger configurations"""

    log_path = core.LOGS_PATH
    Path(log_path).mkdir(exist_ok=True)

    logger: Logger = logging.getLogger(name)
    logger.setLevel(level=logging.INFO)

    # File Handler
    file_formatter = logging.Formatter('%(asctime)s --- %(levelname)s --- %(message)s')

    file_handler = TimedRotatingFileHandler(
        f'{log_path}app.log', backupCount=2, when='midnight', interval=1)

    file_handler.namer = lambda name: name.replace('.log', '') + '.zip'
    file_handler.rotator = zipper
    file_handler.setFormatter(file_formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

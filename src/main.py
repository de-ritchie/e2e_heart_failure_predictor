"""This is the file to execute Feature/Training/Inference Pipeline from CLI"""
import fire

from src.pipeline import feature_pipeline as feat_pipe, \
    inference_pipeline as inf_pipe, \
        training_pipeline as train_pipe

def feature_pipeline():
    """Execute Feature Pipeline"""
    feat_pipe.exec_pipeline()

def training_pipeline():
    """Execute Training Pipeline"""
    train_pipe.exec_pipeline()

def inference_pipeline():
    """Execute Inference Pipeline"""
    inf_pipe.exec_pipeline()

if __name__ == '__main__':
    fire.Fire()

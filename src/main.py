"""This is the file to execute Feature/Training/Inference Pipeline from CLI"""
import fire

from src.pipeline import feature_pipeline, inference_pipeline, training_pipeline

def training():
    """Execute Training Pipeline"""
    training_pipeline.exec_pipeline()

if __name__ == '__main__':
    fire.Fire()

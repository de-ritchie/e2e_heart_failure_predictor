# End-to-End Pipeline of Heart Failure Prediction

## Different types of Pipelines

There are 3 different pipelines used,

- Feature Pipeline - To extract the raw data and push it into the feature store
- Training Pipeline - To fetch the data from feature store and train a ML model
- Inference Pipeline - To predict the results based on the trained model

### Usage

#### Prerequisites

- Python - version 3.10
- Poetry

#### Install dependencies

`poetry install`

#### Executing Training pipeline

`poetry run python -m src.main training`

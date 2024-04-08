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
- Setup cloud MongoDB & obtain the connection string

#### Install dependencies

`poetry install`

#### Set the environment variables

```
MONGO_DB_CONNECTION_STRING=<mongo-db-uri>
MONGO_DB_NAME=<db-name>
FEAT_STORE_COL_NAME=<feature-store-collection-name>
COMET_API_KEY=<comet-api-key>
```

Variables need to configured in the shell/cmd/powershell accordingly

#### Executing Pipelines

- Executing Feature pipeline

  `poetry run python -m src.main feature_pipeline`

- Executing Training pipeline

  `poetry run python -m src.main training_pipeline`

- Executing Inference pipeline: Inference pipeline is under developement

###### Note: The order of pipeline execution matters

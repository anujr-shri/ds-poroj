import pandas as pd
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import os
from src.datascience import logger
from src.datascience.entity.config_entity import ModelEvalutionConfig
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import pickle
import json

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/anujr-shri/ds-poroj.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "anujr-shri"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "385225323cff6f7f9dc0e2cd4b3211fdd7ca6bf7"

class ModelEvalutionComp:
    def __init__(self, config: ModelEvalutionConfig) -> None:
        self.config = config

    def evalution_param(self, test_data, model):
        x_test = test_data.drop([self.config.target_col], axis=1)
        y_test = test_data[[self.config.target_col]]

        y_pred = model.predict(x_test)

        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        logger.info("Caluclated Metrics")
        r2 = r2_score(y_test, y_pred)

        return mae, mse, r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = None
        with open(self.config.model_path, "rb") as file:
            model = pickle.load(file=file)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        scheme = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            logger.info("Logging the info")
            (mae, mse, r2) = self.evalution_param(test_data, model)

            param_dict = {"mae": mae, "mse": mse, "r2": r2}

            with open(self.config.metric_file_name, "w") as file:
                json.dump(param_dict, file)

            mlflow.log_metrics(param_dict)
            mlflow.log_param("alpha", self.config.aplha)
            mlflow.log_param("l1_ratio", self.config.l1_ratio)

            if scheme != "file":

                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")
    



        




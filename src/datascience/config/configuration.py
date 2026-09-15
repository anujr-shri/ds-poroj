# --- This is global configuration manager which configure every step 
# --- It take input from config yaml, schema yaml and params yaml
# --- In config yaml we basically define directory like from where to read and where to write

from src.datascience.constants import *
from src.datascience.entity.config_entity import (DataIngestionConfig, 
                                                  DataTransformationConfig, 
                                                  ModelTraningConfig,
                                                  ModelEvalutionConfig
                                                  )
from src.datascience.utils.common import read_yaml, make_directories

# --- Global Configuration Manager ---
class ConfigurationManager:
    def __init__(self, 
                CONFIG_FILE_PATH=CONFIG_FILE_PATH,
                SCHEMA_FILE_PATH=SCHEMA_FILE_PATH,
                PARAMS_FILE_PATH=PARAMS_FILE_PATH):
        
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.schema = read_yaml(SCHEMA_FILE_PATH)
        self.param = read_yaml(PARAMS_FILE_PATH)

        make_directories([self.config.artifacts_root])

    def get_data_ingetion_config(self) -> DataIngestionConfig:
        data_ingestion_config = self.config.data_ingestion
        make_directories([data_ingestion_config.root_dir])

        data_ingestion_config_obj = DataIngestionConfig(
            **data_ingestion_config
        )

        return data_ingestion_config_obj

    def get_data_transformation_config(self) -> DataTransformationConfig:
        data_trans_config = self.config.data_transformation
        make_directories([data_trans_config.root_dir])

        data_transfomation_config = DataTransformationConfig(
            **data_trans_config
        )

        return data_transfomation_config

    def get_model_traning_config(self) -> ModelTraningConfig:
        config = self.config.model_trainer
        params = self.param.ElasticNet

        make_directories([config.root_dir])

        model_trainer_config = ModelTraningConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = "quality"
        )

        return model_trainer_config

    def get_model_evlaution_config(self) -> ModelEvalutionConfig:
        config = self.config.model_evaluation
        params = self.param.ElasticNet

        make_directories([config.root_dir])

        model_eval_config = ModelEvalutionConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            metric_file_name=config.metric_file_name,
            target_col="quality",
            mlflow_uri="https://dagshub.com/anujr-shri/ds-poroj.mlflow",
            l1_ratio=params.l1_ratio,
            aplha=params.alpha
        )

        return model_eval_config

        




    
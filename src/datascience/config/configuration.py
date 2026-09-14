# --- This is global configuration manager which configure every step 
# --- It take input from config yaml, schema yaml and params yaml
# --- In config yaml we basically define directory like from where to read and where to write

from src.datascience.constants import *
from src.datascience.entity.config_entity import DataIngestionConfig, DataTransformationConfig
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
        




    
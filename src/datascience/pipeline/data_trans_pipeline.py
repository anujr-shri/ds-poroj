from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_trans_comp import DataTransformationComp
from src.datascience import logger

STAGE_NAME="Data Trnasformation Stage"

class DataTransformation:
    def __init__(self):
        pass

    def apply_transformation(self):
        logger.info("started Data Tranformation")
        config_manager = ConfigurationManager()
        data_transformation_config = config_manager.get_data_transformation_config()
        comp = DataTransformationComp(data_transformation_config)
        comp.transform_data()
        logger.info("Ended Data Tranformation")





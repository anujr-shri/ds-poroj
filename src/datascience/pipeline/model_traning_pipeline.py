from src.datascience import logger
from src.datascience.components.model_tarning_comp import ModelTraningComp
from src.datascience.config.configuration import ConfigurationManager

STAGE_NAME = "Model Trainer stage"

class ModelTraning:
    def __init__(self):
        pass

    def start_traning(self):
        logger.info("Start The Traning")
        config_manager = ConfigurationManager()
        model_traning_config = config_manager.get_model_traning_config()
        model_traning_comp = ModelTraningComp(model_traning_config)
        model_traning_comp.train_the_model()
        logger.info("Tranning Completed")


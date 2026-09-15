from src.datascience.components.model_eval_comp import ModelEvalutionComp
from src.datascience.config.configuration import ConfigurationManager
from src.datascience import logger
import os

STAGE_NAME = "Model evaluation stage"

class ModelEvalution:
    def __init__(self) -> None:
        pass

    def run_model_eval(self):
        config_manager = ConfigurationManager()
        model_eval_config = config_manager.get_model_evlaution_config()
        model_evlaution = ModelEvalutionComp(model_eval_config)
        logger.info("Model Evalution Started")
        model_evlaution.log_into_mlflow()
        logger.info("Model Eval Completed")
        logger.info(f"All The info is being tracked in {os.getenv("MLFLOW_TRACKING_URI", "")}")


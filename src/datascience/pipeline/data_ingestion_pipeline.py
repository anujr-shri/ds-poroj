from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingest_comp import DataIngestion
from src.datascience import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config_manager = ConfigurationManager()
        data_ingest_config = config_manager.get_data_ingetion_config()
        data_ingestion_comp = DataIngestion(data_ingest_config)
        logger.info("Start Data Ingestion Pipeline")
        data_ingestion_comp.download_zip_file()
        logger.info("Downloaded The Zip file")
        data_ingestion_comp.extract_zip_file()
        logger.info(f"Extracted The Data from {data_ingest_config.unzip_dir} to {data_ingest_config.local_data_file}")


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e



# --- In This Module we actually decider what each component do like what step are define in a process ---
# --- We just define what to do then we just call it in pipeline module ---
import os
import urllib.request as request
import zipfile
from src.datascience import logger
from src.datascience.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        # --- To Run this component you need to basically provide this config first ---
        self.config = config

    # --- Step 1: Download The zip file ---
    def download_zip_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )

            logger.info(f"{filename} is downloaded")
        else:
            logger.info("Data File Alredy Exsist")

    # --- Step 2: Extract The zip file
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)




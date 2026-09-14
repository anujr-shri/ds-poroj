import pandas as pd
import os
from pathlib import Path
from src.datascience import logger
from src.datascience.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split

class DataTransformationComp:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.root_dir = config.root_dir
        self.data_path = config.data_path

    def transform_data(self):
        data = pd.read_csv(self.data_path)

        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.root_dir, "train_data.csv"), index=False)
        test.to_csv(os.path.join(self.root_dir, "test_data.csv"), index=False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)


        


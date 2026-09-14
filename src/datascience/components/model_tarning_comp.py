from sklearn.linear_model import ElasticNet
from src.datascience.entity.config_entity import ModelTraningConfig
from src.datascience import logger
import pickle
import pandas as pd
import os

class ModelTraningComp:
    def __init__(self, config: ModelTraningConfig):
        self.config = config

    def train_the_model(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        y_train = train_data[[self.config.target_column]]
        x_train = train_data.drop(columns=[self.config.target_column])
        y_test = test_data[[self.config.target_column]]
        x_test = test_data.drop(columns=[self.config.target_column])

        els = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)

        els.fit(x_train, y_train)

        with open(os.path.join(self.config.root_dir, self.config.model_name), 'wb') as file:
            pickle.dump(els, file)
        
        
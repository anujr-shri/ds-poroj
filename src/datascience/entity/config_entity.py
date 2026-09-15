from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: str
    unzip_dir: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: str

@dataclass
class ModelTraningConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str


@dataclass
class ModelEvalutionConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: Path
    aplha: float
    l1_ratio: float
    target_col: str
    mlflow_uri: str




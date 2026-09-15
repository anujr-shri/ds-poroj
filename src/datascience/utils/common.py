import os
import yaml
import json
from src.datascience import logger
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(yaml_path: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(yaml_path, "r") as r:
            content = yaml.safe_load(r)
            logger.info(f"Loaded The yaml file from {yaml_path}")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error("Yaml file is empty")
        raise e
    except Exception as e:
        raise e

@ensure_annotations
def make_directories(direactories_path: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for paths in direactories_path:
        os.makedirs(paths, exist_ok=True)
        if verbose:
            logger.info(f"Create Directory at Path {paths}")




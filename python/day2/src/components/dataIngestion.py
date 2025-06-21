import os 
import sys
# import src.exceptions.exceptions import ProjectException
# import src.logging import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str=os.path.join("raw_file", 'data.csv')

# @dataclass --- this is used to specify only variables not functions

@dataclass
class DataIngestionArtifact:
    raw_data_path: str=os.path.join("raw_file", 'data.csv')
    train_data_path: str=os.path.join("artifacts", 'train.csv')
    test_data_path: str=os.path.join("artifacts", 'test.csv')
    validation_data_path: str=os.path.join("artifacts", 'valid.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        self.artifact_config = DataIngestionArtifact()
        
    def initate_data_ingestion(self):
        logger.logging.info("Data ingestion started")
        try:
            df = pd.read_csv("notebook/data.csv")
            
            logger.logging.info("Dataset read")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.artifact_config.train_data_path), exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path, index= False)
            
            train_set, test_set = train_test_split(df, test_size= 0.2, random_state= 42)
            
            train_set.to_csv(self.artifact_config.train_data_path)
            test_set.to_csv(self.artifact_config.test_data_path)
            
            return(
                self.artifact_config.train_data_path,
                self.artifact_config.test_data_path
            )
            
        except Exception as e:
            logger.logging.error(f"Error during data ingestion: {e}")
            raise ProjectException(e, sys)
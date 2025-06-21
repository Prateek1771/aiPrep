from src.logging import logger
from src.exceptions.exceptions import ProjectException
import sys

from src.components.dataIngestion import DataIngestion

from src.components.dataIngestion import DataIngestionArtifact
from src.components.dataIngestion import DataIngestionConfig

if __name__ == "__main__":
    data_ingestion = DataIngestion()
    train_data, test_data = data_ingestion.initate_data_ingestion()
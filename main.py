from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_obj = DataIngestionTrainingPipeline()
    data_ingestion_obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Preare Base Model"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model_obj =PrepareBaseModelTrainingPipeline()
    prepare_base_model_obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Training"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj =ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Evaluation Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj =EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\n x=======x")
    except Exception as e:
        logger.exception(e)
        raise e
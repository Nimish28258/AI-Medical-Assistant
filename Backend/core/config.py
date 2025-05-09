import os
from dotenv import load_dotenv
import torch

load_dotenv()

class Config:
    """Base Configuration"""

    APP_ENV = os.getenv("APP_ENV", "development")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

    MONGODB_URI = os.getenv("MONGODB_URI")
    if not MONGODB_URI:
        raise ValueError("MONGODB_URI is not set in the environment variables.")

    CLINICAL_BERT_MODEL = os.getenv("CLINICAL_BERT_MODEL")
    BIO_BERT_MODEL = os.getenv("BIO_BERT_MODEL")

    # Automatically select CUDA if available, otherwise fallback to CPU
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    MAX_LEN = int(os.getenv("MAX_LEN", 256))
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", 4))
    THRESHOLD = float(os.getenv("THRESHOLD", 0.5))
    CLASS_NAMES = os.getenv("CLASS_NAMES", "Diagnosis,Prescription,Symptoms,Other").split(",")

    SPACY_MODEL_NAME = os.getenv("SPACY_MODEL_NAME", "en_core_med7_lg")

    SEED = int(os.getenv("SEED", 42))

config = Config()

__all__ = ["config"]

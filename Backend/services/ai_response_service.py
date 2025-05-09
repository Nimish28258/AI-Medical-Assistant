from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
from core.config import config

class AIResponse:
    def __init__(self, model_name: str = config.CLINICAL_BERT_MODEL):
        self.device = torch.device(config.DEVICE)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=len(config.CLASS_NAMES))
        self.model.to(self.device)
        self.model.eval()

    
from typing import Any
from src.models.SentimentModel import Model
from src.models.Summary_model import SummaryModel
import torch
class LLMModel:
    def __init__(self, path_to_sentiment_model, math_2_summary_model):
        self.sentiment_model = Model()
        ckpt = torch.load(path_to_sentiment_model)
        self.sentiment_model.load_state_dict(ckpt["state_dict"])
        
        self.sumary_model = SummaryModel()
        
    def __call__(self, sentences) -> Any:
        sentiment = self.sentiment_model(sentences)
        stop_list = self.sumary_model(sentences)
        return {
            "sentiment":sentiment,
            "stop_list":stop_list
        }
        
        
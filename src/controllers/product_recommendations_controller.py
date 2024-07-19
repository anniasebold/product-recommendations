import pandas as pd
from src.config import Config
from typing import Dict


class ProductRecommendationsController:
    """
        Responsibility for implementing the product recommendation logic
    """
    def __init__(self):
        self.df = pd.read_csv(Config.FILE_PATH, sep=',')

    def get_recommendations(self) -> Dict:
        return {
            "recommendations": "recommendations"
        }

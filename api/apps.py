import os
import joblib
from django.apps import AppConfig
from django.conf import settings
import pandas as pd


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "svdModel.joblib")
    RECOMMENDATION_SYSTEM = os.path.join(settings.MODELS, "generate_prediction.joblib")
    data_path = os.path.join(settings.MODELS, "books.csv")
    books_metadata = pd.read_csv(data_path)
    model = joblib.load(MODEL_FILE)

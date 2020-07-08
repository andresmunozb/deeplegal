from .eval import evaluate_one
from .eval import cfg
from .models import CRNN_STN


class Predictor:

    def __init__(self, model_path):
        _, model = CRNN_STN(cfg)    
        model.load_weights(model_path)
        self.model = model

    def predict(self, img_path):
        return evaluate_one(self.model, [img_path])

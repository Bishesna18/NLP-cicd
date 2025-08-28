# test_predict.py
from predict import predict_sentiment
import numpy as np

def test_positive():
    pred = predict_sentiment("I absolutely loved this movie, it was amazing!")
    # ensure we got a 0/1 back
    assert isinstance(pred, np.ndarray)
    assert pred.shape == (1,)
    # Expect positive (1)
    assert pred[0] in (0,1)
    # If your model is good, this should be positive:
    assert pred[0] == 1

def test_negative():
    pred = predict_sentiment("This was a horrible film. Boring and badly acted.")
    assert isinstance(pred, np.ndarray)
    assert pred.shape == (1,)
    assert pred[0] in (0,1)
    # Expect negative (0)
    assert pred[0] == 0

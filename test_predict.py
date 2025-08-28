from predict import predict_sentiment

def test_positive():
    assert predict_sentiment("I love this movie!")[0] == 1

def test_negative():
    assert predict_sentiment("I dont like this film!")[0] == 0


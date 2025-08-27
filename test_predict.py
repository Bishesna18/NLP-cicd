from predict import predict_sentiment

def test_positive():
    assert predict_sentiment("I love this movie!")[0] == 1

def test_negative():
    assert predict_sentiment("I hate this film!")[0] == 0

def run_all_tests():
    test_positive()
    test_negative()
    print("All tests passed!")

if __name__ == "__main__":
    run_all_tests()


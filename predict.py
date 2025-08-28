# predict.py
import joblib
from typing import List, Union

MODEL_PATH = "sentiment_model.pkl"
VECTORIZER_PATH = "tfidf_vectorizer.pkl"

def load_model(model_path=MODEL_PATH):
    return joblib.load(model_path)

def load_vectorizer(vec_path=VECTORIZER_PATH):
    return joblib.load(vec_path)

def predict_sentiment(texts: Union[str, List[str]]):
    if isinstance(texts, str):
        texts = [texts]
    try:
        # Try pipeline model
        model = load_model()
        return model.predict(texts)
    except Exception:
        # Fallback: separate vectorizer + model
        vectorizer = load_vectorizer()
        model = load_model()
        X = vectorizer.transform(texts)
        return model.predict(X)

if __name__ == "__main__":
    print(predict_sentiment("I love this movie!"))

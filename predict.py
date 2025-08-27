import joblib

def load_model(model_path='sentiment_model.pkl'):
    """Load the trained sentiment model"""
    return joblib.load(model_path)

def predict_sentiment(text, model_path='sentiment_model.pkl'):
    """Predict sentiment for a single text"""
    model = load_model(model_path)
    return model.predict([text])[0]

# Example usage
if __name__ == "__main__":
    sample_text = "I love this movie!"
    prediction = predict_sentiment(sample_text)
    print(f"Text: {sample_text}")
    print(f"Predicted Sentiment: {'positive' if prediction == 1 else 'negative'}")

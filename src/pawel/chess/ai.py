from transformers import pipeline


def classify_text(text):
    # Load a pre-trained sentiment-analysis pipeline
    classifier = pipeline('sentiment-analysis')

    # Classify the input text
    result = classifier(text)

    return result


if __name__ == "__main__":
    # Example text
    text = "I love programming with Python!"

    # Classify the text
    classification = classify_text(text)

    # Print the result
    print(f"Text: {text}")
    print(f"Classification: {classification}")

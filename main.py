from textblob import TextBlob

print("🧠 Welcome to Sentiment Analyzer!")
print("Type 'exit' to quit.\n")

while True:
    text = input("Enter a sentence: ")

    if text.lower() == 'exit':
        print("Goodbye! 👋")
        break

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        print("🙂 Sentiment: Positive\n")
    elif polarity < 0:
        print("🙁 Sentiment: Negative\n")
    else:
        print("😐 Sentiment: Neutral\n")

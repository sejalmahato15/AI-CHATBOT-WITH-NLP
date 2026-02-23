import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Ensure downloads
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

greetings = ["hello", "hi", "hey"]
greeting_responses = ["Hello!", "Hi there!", "Hey!"]

knowledge_base = {
    "python": "Python is a programming language.",
    "nlp": "NLP means Natural Language Processing.",
    "ai": "AI stands for Artificial Intelligence.",
    "internship": "Internship helps you gain practical experience.",
    "name": "I am your AI Chatbot."
}

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in string.punctuation]
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    return tokens

def chatbot():
    print("AI Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Bot: Goodbye!")
            break

        if user_input.lower() in greetings:
            print("Bot:", greeting_responses[0])
            continue

        tokens = preprocess(user_input)

        found = False
        for word in tokens:
            if word in knowledge_base:
                print("Bot:", knowledge_base[word])
                found = True
                break

        if not found:
            print("Bot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()

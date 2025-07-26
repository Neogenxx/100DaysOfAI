import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you today?"]
    ],
    [
        r"what is your name ?",
        ["I'm a simple rule-based AI chatbot."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm just a bunch of code, but I'm fine!"]
    ],
    [
        r"sorry (.*)",
        ["No worries.", "It's okay, no need to apologize."]
    ],
    [
        r"i'm (.*)",
        ["Nice to meet you %1! How can I help you today?"]
    ],
    [
        r"(.*) help (.*)",
        ["I’d be happy to help! Could you please give me more details?"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you using simple rule-based logic."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm everywhere. I'm cloud-based!"]
    ],
    [
        r"quit",
        ["Goodbye! It was nice talking to you.", "Take care!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you rephrase?", "Interesting... Tell me more."]
    ]
]

def start_chat():
    print("🤖 Chatbot: Hello! Type 'quit' to end the conversation.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    start_chat()

import json
import string
from random import choice
import nltk
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('english', True)
not_wanted = ['?', '!', ',', '.']

with open('conversation.json', 'r') as f:
    conversation = json.load(f)


def probability(user_words, known_words):
    certainty = 0
    for word in user_words:
        if word in known_words:
            certainty += 1
    percentage = float(certainty / len(known_words)) * 100
    return percentage


def check_responses(msg):
    type_percentages = {}

    for conv in conversation['conversation']:
        translator = str.maketrans('', '', string.punctuation)
        sentences = [sentence.translate(translator) for sentence in conv['user']]
        single_words = [word.lower() for sentence in sentences for word in sentence.split()]
        probabilities = [probability(msg,single_words)]
        type_percentages[conv['type']] = probabilities[0]
    return type_percentages


def response(user_in):
    words = [stemmer.stem(w.lower()) for w in nltk.word_tokenize(user_in)]
    type_percentages = check_responses(words)
    best_type = max(type_percentages, key=type_percentages.get)
    # print(type_percentages)
    return best_type


while True:
    response_type = response(input('You: '))
    # print(response_type)
    response_list = next((conv['bot'] for conv in conversation['conversation'] if response_type in conv['type']), [])
    if response_list:
        print(f'Bot: {choice(response_list)}')
    else:
        print('Bot: Sorry, but I did not understand that.')

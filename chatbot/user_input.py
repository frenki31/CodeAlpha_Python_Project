import nltk
import numpy as np
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('english')


def get_words(sentence):
    return [stemmer.stem(word.lower() for word in nltk.word_tokenize(sentence))]

def binary_words(sentence, words):
    words_sentence = get_words(sentence)
    binary = [0]*len(words)
    for word in words_sentence:
        for index, w in enumerate(words):
            if word == w:
                binary[index] = 1
    return np.array(binary)

def predict(user_sentence, model):
    pass
    # binary = binary_words(user_sentence, words)
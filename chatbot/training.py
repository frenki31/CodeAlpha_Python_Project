import json
import nltk
import random
import numpy as np
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer('english')
not_wanted = ['?', '.', ',', '!']

with open('conversation.json', 'r') as file:
    conversation = json.load(file)

tokenized_words = []
word_type = []
classes = []
for conv in conversation['conversation']:
    for user in conv['user']:
        word = nltk.word_tokenize(user)
        tokenized_words.extend(word)
        word_type.append((word, conv['type']))
        if conv['type'] not in classes:
            classes.append(conv['type'])

tokenized_words = [stemmer.stem(word.lower()) for word in tokenized_words if word not in not_wanted]
tokenized_words = sorted(set(tokenized_words))
classes = sorted(set(classes))

x_train = []
y_train = []
empty_output_array = [0] * len(classes)
for word in word_type:
    word_binary = []
    user_words = word[0]
    user_words = [stemmer.stem(w.lower()) for w in user_words]
    for t_word in tokenized_words:
        word_binary.append(1) if t_word in user_words else word_binary.append(0)
    output = list(empty_output_array)
    output[classes.index(word[1])] = 1
    x_train.append(word_binary)
    y_train.append(output)
random.shuffle(x_train)
random.shuffle(y_train)
x_train = np.array(x_train)
y_train = np.array(y_train)

print('Training data created')

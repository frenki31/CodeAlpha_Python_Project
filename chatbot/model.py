from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Dense, Activation, Dropout
from training import *

model = Sequential()
model.add(Dense(128, input_shape=(len(x_train[0]),), activation='relu'))
model.add(Dropout(0,5))
model.add(Dense(64, 'relu'))
model.add(Dropout(0,5))
model.add(Dense(len(y_train[0]),'softmax'))

adam = Adam(learning_rate=0.001,ema_momentum=0.9)
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

fit = model.fit(x_train, y_train, 5, 200, 1)
model.save('chatbot.keras', fit)
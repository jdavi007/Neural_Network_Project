import random
import numpy as np
import tensorflow
from keras.models import Sequential
from keras.layers import LSTM, Dense, Activation
from keras.optimizers import RMSprop

# Importing and preparing data
text_file = open('LOTR.txt', 'r', encoding="ISO_8859-1")
text = text_file.read()
text_file.close()
characters = sorted(set(text))  # pulls characters from txt file and sorts them
char_to_index = dict((c, i) for i, c in enumerate(characters))  # used for converting text to numerical values
index_to_char = dict((i, c) for i, c in enumerate(characters))

SEQ_LENGTH = 40
STEP_SIZE = 3
sentences = []
next_characters = []

#Neural Network
for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
  sentences.append(text[i: i + SEQ_LENGTH])
  next_characters.append(text[i + SEQ_LENGTH])

x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)), dtype=bool)
y = np.zeros((len(sentences), len(characters)), dtype=bool)

for i, sentence in enumerate(sentences):
  for t, character in enumerate(sentence):
    x[i, t, char_to_index[character]] = 1
  y[i, char_to_index[next_characters[i]]] = 1

# Building NN
model = Sequential()
model.add(LSTM(128, input_shape=(SEQ_LENGTH, len(characters))))
model.add(Dense(len(characters)))
model.add(Activation('softmax'))

# Training NN
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(learning_rate=0.01))
model.fit(x, y, batch_size=256, epochs=4)

#Saves trained NN so dont have to train every run
model.save('textgenerator.model')

#Loads saved NN
model = tensorflow.keras.models.load_model('textgenerator.model')


def sample(preds, temperature=1.0):
  preds = np.asarray(preds).astype('float64')
  preds = np.log(preds) / temperature
  exp_preds = np.exp(preds)
  preds = exp_preds / np.sum(exp_preds)
  probas = np.random.multinomial(1, preds, 1)
  return np.argmax(probas)


def generate_text(length, temperature):
  # Copy first few characters and NN predicts what comes next
  start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
  generated = ''
  sentence = text[start_index: start_index + SEQ_LENGTH]

#This makes the first word a full word - this doesnt work
  if sentence[0] != " ":
    while sentence[0] != " ":
      start_index += 1
      sentence = text[start_index: start_index + SEQ_LENGTH]

  generated += sentence

  for i in range(length):
    x = np.zeros((1, SEQ_LENGTH, len(characters)))
    for t, character in enumerate(sentence):
      x[0, t, char_to_index[character]] = 1

    predictions = model.predict(x, verbose=0)[0]
    next_index = sample(predictions, temperature)
    next_character = index_to_char[next_index]

    generated += next_character
    sentence = sentence[1:] + next_character

  return generated

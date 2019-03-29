# -*- coding: utf-8 -*-

import src.parser.toml as tml

from keras.models import Sequential
from keras.layers import Dense#, Conv1D

def _init():
    model = Sequential()
    model.add(Dense(tml.value('audio','s_len'), input_dim=tml.value('audio','s_len')))
    #model.add(Conv1D(16, tml.value('audio', 'frame_size'), strides=tml.value('audio', 'hop_size'), input_dim=tml.value('audio','s_len')))
    return model

def _compile(model):
    model.compile(tml.value('neuralnet', 'optimizer'), tml.value('neuralnet', 'loss'), ['accuracy'])

def _train(model, data, labels):
    model.fit(data, labels, tml.value('neuralnet', 'batch_size'), tml.value('neuralnet', 'epochs'))

def _predict(model, data):
    return model.predict(data, tml.value('neuralnet', 'batch_size'))

def _evaluate(model, data, labels):
    return model.evaluate(data, labels, tml.value('neuralnet', 'batch_size'))

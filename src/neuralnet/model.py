# -*- coding: utf-8 -*-

import src.parser.toml as tml
import src.utils.logger as log

from keras.models import Sequential
from keras.layers import Dense

def _init():
    log.debug("Building model")
    model = Sequential()
    model.add(Dense(tml.value('audio','s_len'), input_dim=tml.value('audio','s_len')))
    return model

def _compile(model):
    log.debug("Compiling model")
    model.compile(tml.value('neuralnet', 'optimizer'), tml.value('neuralnet', 'loss'), ['accuracy'])

def _train(model, data, labels):
    log.debug("Training model")
    model.fit(data, labels, tml.value('neuralnet', 'batch_size'), tml.value('neuralnet', 'epochs'))

def _predict(model, data):
    log.debug("Generating predictions")
    return model.predict(data, tml.value('neuralnet', 'batch_size'))

def _evaluate(model, data, labels):
    log.debug("Evaluating model")
    return model.evaluate(data, labels, tml.value('neuralnet', 'batch_size'))

def _save(model):
    model.save(tml.value('neuralnet', 'model_fname'))

# -*- coding: utf-8 -*-

import src.parser.toml as tml
import src.utils.logger as log

from keras.models import Sequential
from keras.layers import Conv1D, Activation


class NeuralNetwork(object):
    def __init__(self):
        log.debug("Building model")
        self.optimizer = tml.value('neuralnet', 'optimizer')
        self.loss = tml.value('neuralnet', 'loss')
        self.batch_size = tml.value('neuralnet', 'batch_size')
        self.epochs = tml.value('neuralnet', 'epochs')
        self.metrics = tml.value('neuralnet', 'metrics')
        self.input_len = tml.value('audio', 's_len')
        self.fname = tml.value('neuralnet', 'model_fname')
        self.model = Sequential()
        self.model.add(Conv1D(1, 4096, strides=1, padding='same', input_shape=(self.input_len, 1)))
        self.model.add(Activation('relu'))
        
    def compile(self):
        log.debug("Compiling model")
        self.model.compile(self.optimizer, self.loss, self.metrics)

    def train(self, data, labels):
        log.debug("Training model")
        self.model.fit(data, labels, self.batch_size, self.epochs)

    def predict(self, data):
        log.debug("Generating predictions")
        return self.model.predict(data, self.batch_size)

    def evaluate(self, data, labels):
        log.debug("Evaluating model")
        return self.model.evaluate(data, labels, self.batch_size)

    def save(self):
        log.debug("Saving model")
        self.model.save(self.fname)

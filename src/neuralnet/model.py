# -*- coding: utf-8 -*-

import src.parser.toml as tml
import src.utils.logger as log
import src.neuralnet.config as cfg

from keras.models import Sequential
from keras.layers import Input, Conv1D


def _model_(input_shape, batch_size=None):
    model = Sequential()
    model.add(Input(batch_shape=(batch_size, *input_shape)))
    model.add(Conv1D(4, input_shape[0] // 10, strides=4, padding='causal'))
    return model


class NeuralNetwork(object):
    def __init__(self):
        log.debug("Building model")
        self.batch_size = cfg.BATCH_SIZE
        self.epochs = cfg.EPOCHS
        self.input_shape = cfg.INPUT_SHAPE
        self.optimizer = cfg.OPTIMIZER
        self.loss = cfg.LOSS
        self.initializer = cfg.INITIALIZER
        self.metrics = cfg.METRICS
        self.fname = tml.value('neuralnet', 'fname')
        self.model = _model_(self.input_shape)
        
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

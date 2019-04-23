# -*- coding: utf-8 -*-

import src.utils.logger as log
import src.neuralnet.config as cfg
from src.neuralnet.utils import split_valid
import src.neuralnet.network as net


class NeuralNetwork(object):
    def __init__(self, model=None):
        self.bsiz = cfg.BATCH_SIZE
        self.epoc = cfg.EPOCHS
        self.ishp = cfg.INPUT_SHAPE
        self.ksiz = cfg.KERNEL_SIZE
        self.opti = cfg.OPTIMIZER
        self.loss = cfg.LOSS
        self.kini = cfg.KERNEL_INITIALIZER
        self.bini = cfg.BIAS_INITIALIZER
        self.metr = cfg.METRICS
        self.cbac = cfg.CALLBACKS
        self.model = net.onelayer1DConvTranspose(self.bsiz, self.ishp, self.ksiz) if model is None else model
        
    def compile(self):
        log.debug("Compiling model")
        self.model.compile(self.opti, loss=self.loss, metrics=self.metr)

    def train(self, data, labels):
        log.debug("Training model")
        train_data, valid_data = split_valid(data, labels)
        self.model.fit(*train_data, batch_size=self.bsiz, epochs=self.epoc, callbacks=self.cbac, validation_data=valid_data)

    def predict(self, data):
        log.debug("Generating predictions")
        return self.model.predict(data, batch_size=self.bsiz)

    def evaluate(self, data, labels):
        log.debug("Evaluating model")
        return self.model.evaluate(data, labels, batch_size=self.bsiz, callbacks=self.cbac)

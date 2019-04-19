# -*- coding: utf-8 -*-

import src.utils.logger as log
import src.neuralnet.config as cfg
from src.neuralnet.utils import split, Conv1DTranspose

from keras.models import Model
from keras.layers import Input, Conv1D, MaxPooling1D, UpSampling1D


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
        if model is None:
            self.__model__()
        else:
            self.model = model

    def __model__(self):
        log.debug("Building model")
        ## input

        X = Input(batch_shape=(self.bsiz, *self.ishp))

        # encoder
        """
        ENC = Conv1D(2, self.ksiz, padding='same', activation='tanh', kernel_initializer=self.kini, bias_initializer=self.bini)(X)
        ENC = MaxPooling1D(2, padding='same')(ENC)
        ENC = Conv1D(4, self.ksiz, padding='same', activation='tanh', kernel_initializer=self.kini, bias_initializer=self.bini)(ENC)
        ENC = MaxPooling1D(2, padding='same')(ENC)
        """
        # decoder

        DEC = Conv1D(8, self.ksiz, strides=2, padding='same', activation='tanh', kernel_initializer=self.kini, bias_initializer=self.bini)(X)
        DEC = UpSampling1D(2)(DEC)
        DEC = Conv1D(4, self.ksiz, strides=2, padding='same', activation='tanh', kernel_initializer=self.kini, bias_initializer=self.bini)(DEC)
        DEC = UpSampling1D(2)(DEC)

        ## output

        Y = Conv1D(1, self.ksiz, padding='same', activation='linear', kernel_initializer=self.kini, bias_initializer=self.bini)(X)

        # model

        self.model = Model(inputs=X, outputs=Y)
        
    def compile(self):
        log.debug("Compiling model")
        self.model.compile(self.opti, loss=self.loss, metrics=self.metr)

    def train(self, data, labels):
        log.debug("Training model")
        _train, _valid = split(data, labels)
        self.model.fit(*_train, batch_size=self.bsiz, epochs=self.epoc, callbacks=self.cbac, validation_data=_valid)

    def predict(self, data):
        log.debug("Generating predictions")
        return self.model.predict(data, batch_size=self.bsiz)

    def evaluate(self, data, labels):
        log.debug("Evaluating model")
        return self.model.evaluate(data, labels, batch_size=self.bsiz, callbacks=self.cbac)

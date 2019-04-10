# -*- coding: utf-8 -*-

import src.utils.logger as log
import src.neuralnet.config as cfg

from keras.models import Model
from keras.layers import Input, Conv1D, MaxPooling1D, UpSampling1D


class NeuralNetwork(object):
    def __init__(self):
        self.b_siz = cfg.BATCH_SIZE
        self.epoc = cfg.EPOCHS
        self.in_shp = cfg.INPUT_SHAPE
        self.k_siz = cfg.KERNEL_SIZE
        self.v_spl = cfg.VALIDATION_SPLIT
        self.opt = cfg.OPTIMIZER
        self.loss = cfg.LOSS
        self.k_ini = cfg.KERNEL_INITIALIZER
        self.b_ini = cfg.BIAS_INITIALIZER
        self.met = cfg.METRICS
        self.c_bac = cfg.CALLBACKS
        self.fnam = cfg.FILE_NAME
        self.__model__()

    def __model__(self):
        log.debug("Building model")
        ## input

        X = Input(batch_shape=(self.b_siz, *self.in_shp))

        # encoder

        ENC = Conv1D(2, self.k_siz, input_shape=self.in_shp, padding='causal', activation='tanh', kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(X)
        ENC = MaxPooling1D(2, padding='same')(ENC)
        ENC = Conv1D(4, self.k_siz, padding='same', activation='tanh', kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(ENC)
        ENC = MaxPooling1D(2, padding='same')(ENC)
        
        # decoder

        DEC = Conv1D(8, self.k_siz, padding='same', activation='tanh', kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(ENC)
        DEC = UpSampling1D(2)(DEC)
        DEC = Conv1D(4, self.k_siz, padding='same', activation='tanh', kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(DEC)
        DEC = UpSampling1D(2)(DEC)

        ## output

        Y = Conv1D(1, self.k_siz, padding='same', activation='linear', kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(DEC)

        # model

        self.model = Model(inputs=X, outputs=Y)
        
    def compile(self):
        log.debug("Compiling model")
        self.model.compile(self.opt, loss=self.loss, metrics=self.met)

    def train(self, data, labels):
        log.debug("Training model")
        self.model.fit(data, labels, batch_size=self.b_siz, epochs=self.epoc, callbacks=[self.c_bac], validation_split=self.v_spl)

    def predict(self, data):
        log.debug("Generating predictions")
        return self.model.predict(data, batch_size=self.b_siz)

    def evaluate(self, data, labels):
        log.debug("Evaluating model")
        return self.model.evaluate(data, labels, batch_size=self.b_siz, callbacks=[self.c_bac])

    def save(self):
        log.debug("Saving model")
        self.model.save(self.fnam)

# -*- coding: utf-8 -*-

import src.parser.toml as tml
import src.utils.logger as log
import src.neuralnet.config as cfg

from keras.models import Model
from keras.layers import Input, Conv1D, MaxPooling1D, UpSampling1D


class NeuralNetwork(object):
    def __init__(self):
        self.b_siz = cfg.BATCH_SIZE
        self.epoc = cfg.EPOCHS
        self.in_shp = cfg.INPUT_SHAPE
        self.k_nbr = cfg.KERNEL_NUMBER
        self.k_siz = cfg.KERNEL_SIZE
        self.opt = cfg.OPTIMIZER
        self.loss = cfg.LOSS
        self.h_act = cfg.HIDDEN_ACTIVATION
        self.f_act = cfg.FINAL_ACTIVATION
        self.k_ini = cfg.KERNEL_INITIALIZER
        self.b_ini = cfg.BIAS_INITIALIZER
        self.met = cfg.METRICS
        self.fnam = tml.value('neuralnet', 'fname')
        self.__model__()

    def __model__(self):
        log.debug("Building model")
        ## input

        X = Input(batch_shape=(self.b_siz, *self.in_shp))

        # encoder

        ENC = Conv1D(self.k_nbr, self.k_siz, input_shape=*self.in_shp, padding='causal', activation=self.h_act, kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(X)
        ENC = MaxPooling1D(2, padding='same')(ENC)
        ENC = Conv1D(2 * self.k_nbr, self.k_siz, padding='same', activation=self.h_act, kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(ENC)
        ENC = MaxPooling1D(2, padding='same')(ENC)
        ENC = Conv1D(4 * self.k_nbr, self.k_siz, padding='same', activation=self.h_act, kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(ENC)
        
        # decoder

        DEC = Conv1D(4 * self.k_nbr, self.k_siz, padding='same', activation=self.h_act, kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(ENC)
        DEC = UpSampling1D(2)(DEC)
        DEC = Conv1D(2 * self.k_nbr, self.k_siz, padding='same', activation=self.h_act, kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(DEC)
        DEC = UpSampling1D(2)(DEC)

        ## output

        Y = Conv1D(1, self.k_siz, padding='same', activation=self.f_act, kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(DEC)

        self.model = Model(inputs=X, outputs=Y)
        
    def compile(self):
        log.debug("Compiling model")
        self.model.compile(self.opt, self.loss, self.met)

    def train(self, data, labels):
        log.debug("Training model")
        self.model.fit(data, labels, self.b_siz, self.epoc)

    def predict(self, data):
        log.debug("Generating predictions")
        return self.model.predict(data, self.b_siz)

    def evaluate(self, data, labels):
        log.debug("Evaluating model")
        return self.model.evaluate(data, labels, self.b_siz)

    def save(self):
        log.debug("Saving model")
        self.model.save(self.fnam)

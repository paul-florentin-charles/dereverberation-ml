# -*- coding: utf-8 -*-

import src.parser.toml as tml
import src.utils.logger as log
import src.neuralnet.config as cfg
from src.neuralnet.utils import shaped

from keras.models import Model
from keras.layers import Input, Conv1D, MaxPooling1D, UpSampling1D


class NeuralNetwork(object):
    def __init__(self):
        self.b_siz = cfg.BATCH_SIZE
        self.epoc = cfg.EPOCHS
        self.in_shp = cfg.INPUT_SHAPE
        self.f_siz = cfg.FRAME_SIZE
        self.opt = cfg.OPTIMIZER
        self.loss = cfg.LOSS
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

        ENC = Conv1D(16, self.f_siz, padding='causal', activation='relu', kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(X)
        ENC = MaxPooling1D(2, padding='same')(ENC)
        ENC = Conv1D(8, self.f_siz, padding='causal', activation='relu', kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(ENC)
        ENC = MaxPooling1D(2, padding='same')(ENC)
        ENC = Conv1D(4, self.f_siz, padding='causal', activation='relu', kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(ENC)
        ENC = MaxPooling1D(2, padding='same')(ENC)

        # decoder

        DEC = Conv1D(4, self.f_siz, padding='causal', activation='relu', kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(ENC)
        DEC = UpSampling1D(2)(DEC)
        DEC = Conv1D(8, self.f_siz, padding='causal', activation='relu', kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(DEC)
        DEC = UpSampling1D(2)(DEC)
        DEC = Conv1D(16, self.f_siz, padding='causal', activation='relu', kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(DEC)
        DEC = UpSampling1D(2)(DEC)

        ## output

        Y = Conv1D(1, self.frame_size, padding='causal', activation='sigmoid', kernel_initializer=self.k_ini, bias_initializer=self.b_ini)(DEC)

        self.model = Model(inputs=X, outputs=Y)
        
    def compile(self):
        log.debug("Compiling model")
        self.model.compile(self.opt, self.loss, self.met)

    def train(self, data, labels):
        log.debug("Training model")
        self.model.fit(*map(shaped, (data, labels)), self.b_siz, self.epoc)

    def predict(self, data):
        log.debug("Generating predictions")
        return self.model.predict(shaped(data), self.b_siz)

    def evaluate(self, data, labels):
        log.debug("Evaluating model")
        return self.model.evaluate(*map(shaped, (data, labels)), self.b_siz)

    def save(self):
        log.debug("Saving model")
        self.model.save(self.fnam)

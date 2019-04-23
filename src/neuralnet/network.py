# -*- coding: utf-8 -*-

from src.neuralnet.utils import Conv1DTranspose

from keras.models import Model
from keras.layers import Input, Conv1D, MaxPooling1D, UpSampling1D


def autoencoder1DTranspose(batch_size, input_shape, frame_size):
    X = Input(batch_shape=(batch_size, *input_shape))

    ENC = Conv1D(8, frame_size, strides=2, padding='same', activation='tanh', kernel_initializer='truncated_normal', bias_initializer='truncated_normal')(X)
    ENC = Conv1D(4, frame_size, strides=2, padding='same', activation='tanh', kernel_initializer='truncated_normal', bias_initializer='truncated_normal')(ENC)
    
    DEC = Conv1DTranspose(ENC, 2, frame_size, strides=2, padding='same', activation='tanh', kernel_initializer='truncated_normal', bias_initializer='truncated_normal')
    DEC = Conv1DTranspose(DEC, 4, frame_size, strides=2, padding='same', activation='tanh', kernel_initializer='truncated_normal', bias_initializer='truncated_normal')
    
    Y = Conv1DTranspose(DEC, 1, frame_size, padding='same', activation='linear', kernel_initializer='truncated_normal', bias_initializer='truncated_normal')
    
    return Model(inputs=X, outputs=Y)

def autoencoder1D(batch_size, input_shape, frame_size):
    X = Input(batch_shape=(batch_size, *input_shape))

    ENC = Conv1D(8, frame_size, padding='same', activation='tanh', kernel_initializer='truncated_normal', bias_initializer='truncated_normal')(X)
    ENC = MaxPooling1D(2, padding='same')(ENC)
    ENC = Conv1D(4, frame_size, padding='same', activation='tanh', kernel_initializer='truncated_normal', bias_initializer='truncated_normal')(ENC)
    ENC = MaxPooling1D(2, padding='same')(ENC)

    DEC = Conv1D(2, frame_size, padding='same', activation='tanh', kernel_initializer='truncated_normal', bias_initializer='truncated_normal')(ENC)
    DEC = UpSampling1D(2)(DEC)
    DEC = Conv1D(4, frame_size, padding='same', activation='tanh', kernel_initializer='truncated_normal', bias_initializer='truncated_normal')(DEC)
    DEC = UpSampling1D(2)(DEC)
    
    Y = Conv1D(1, frame_size, padding='same', activation='linear', kernel_initializer='truncated_normal', bias_initializer='truncated_normal')(DEC)
    
    return Model(inputs=X, outputs=Y)

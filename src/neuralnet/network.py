# -*- coding: utf-8 -*-

from src.neuralnet.utils import Conv1DTranspose

from keras.models import Model
from keras.layers import Input, Conv1D, MaxPooling1D, UpSampling1D

def convAutoencoder1D(batch_size, input_shape, frame_size, n_layers=5):
    X = Input(batch_shape=(batch_size, *input_shape))

    ENC = convEncoder1D(X, frame_size, n_layers=int(n_layers/2))

    DEC = convDecoder1D(ENC, frame_size, n_layers=int(n_layers/2))
    
    Y = Conv1D(1, frame_size, padding='same', activation='linear', kernel_initializer='truncated_normal')(DEC)
    
    return Model(inputs=X, outputs=Y)

def deconvAutoencoder1D(batch_size, input_shape, frame_size, n_layers=5):
    X = Input(batch_shape=(batch_size, *input_shape))

    ENC = deconvEncoder1D(X, frame_size, n_layers=int(n_layers/2))
    
    DEC = deconvDecoder1D(ENC, frame_size, n_layers=int(n_layers/2))
    
    Y = Conv1DTranspose(DEC, 1, frame_size, padding='same', activation='linear', kernel_initializer='truncated_normal')
    
    return Model(inputs=X, outputs=Y)

def convEncoder1D(input_tensor, frame_size, n_layers=2):
    if n_layers == 0:
        return input_tensor
    
    encoder = Conv1D(2, frame_size, padding='same', activation='tanh', kernel_initializer='truncated_normal')(input_tensor)
    encoder = MaxPooling1D(2, padding='same')(encoder)
    for idx in range(1, n_layers):
        encoder = Conv1D(2**(idx + 1), frame_size, padding='same', activation='tanh', kernel_initializer='truncated_normal')(encoder)
        encoder = MaxPooling1D(2, padding='same')(encoder)

    return encoder

def convDecoder1D(input_tensor, frame_size, n_layers=2):
    if n_layers == 0:
        return input_tensor
    
    decoder = Conv1D(2**(n_layers + 1), frame_size, padding='same', activation='tanh', kernel_initializer='truncated_normal')(input_tensor)
    decoder = UpSampling1D(2)(decoder)
    for idx in range(n_layers, 1, -1):
        decoder = Conv1D(2**idx, frame_size, padding='same', activation='tanh', kernel_initializer='truncated_normal')(decoder)
        decoder = UpSampling1D(2)(decoder)

    return decoder

def deconvEncoder1D(input_tensor, frame_size, n_layers=2):
    if n_layers == 0:
        return input_tensor
    
    encoder = Conv1D(2, frame_size, strides=2, padding='same', activation='tanh', kernel_initializer='truncated_normal')(input_tensor)
    for idx in range(1, n_layers):
        encoder = Conv1D(2**(idx + 1), frame_size, strides=2, padding='same', activation='tanh', kernel_initializer='truncated_normal')(encoder)

    return encoder

def deconvDecoder1D(input_tensor, frame_size, n_layers=2):
    if n_layers == 0:
        return input_tensor
    
    decoder = Conv1DTranspose(input_tensor, 2**(n_layers + 1), frame_size, strides=2, padding='same', activation='tanh', kernel_initializer='truncated_normal')
    for idx in range(n_layers, 1, -1):
        decoder = Conv1DTranspose(decoder, 2**idx, frame_size, strides=2, padding='same', activation='tanh', kernel_initializer='truncated_normal')

    return decoder

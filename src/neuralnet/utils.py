# -*- coding: utf-8 -*-

"""Data shaping related to I/O of Neural Network.

Along with a function to pick up best model.
"""

import src.utils.logger as log
import src.utils.path as pth
import src.parser.toml as tml
from src.datagen.utils import __pcm2float, __float2pcm
import src.neuralnet.config as cfg

import keras.backend as K
from keras.models import load_model
from keras.layers import Conv2DTranspose, Lambda


def Conv1DTranspose(input_tensor, filters, kernel_size, strides=1, padding='same'):
    X = Lambda(lambda x: K.expand_dims(x, axis=2))(input_tensor)
    X = Conv2DTranspose(filters=filters, kernel_size=(kernel_size, 1), strides=(strides, 1), padding=padding)(X)
    X = Lambda(lambda x: K.squeeze(x, axis=2))(X)
    return X

#TODO: Implement 2d-representation for data, to test a model with spectrum
    
def shape(data):
    """Shape <data> to fit input of neural network."""
    log.debug("Shaping data")
    
    if data.ndim != 2:
        log.error("\'shape\' expects a two-dimensional array : (n_samples, sample_len)")
        return data

    _dtype = 'int{0}'.format(tml.value('bit_depth', section='audio'))
    
    if data.dtype != _dtype:
        log.warning("\'shape\' expects an {0} array".format(_dtype))
        
    data = data.astype('float64')
    for i in range(data.shape[0]):
        data[i] = __pcm2float(data[i].astype(_dtype))

    return data.reshape(*data.shape, 1)    

def unshape(data):
    """Unshape <data> output of neural network."""
    log.debug("Unshaping data")
    
    if data.ndim != 3:
        log.error("\'unshape\' expects a three-dimensional array : (n_samples, sample_len, n_channels)")
        return data

    data = data.reshape(*data.shape[:-1])

    if data.dtype.kind != 'f':
        log.warning("\'unshape\' expects a float array")
        data = data.astype('float64')

    for i in range(data.shape[0]):
        data[i] = __float2pcm(data[i])

    return data.astype('int{0}'.format(tml.value('bit_depth', section='audio')))

def split(data, labels):
    n_train = cfg.BATCH_SIZE * int((1 - cfg.VALIDATION_SPLIT) * data.shape[0] / cfg.BATCH_SIZE)
    tdata, tlabels = data[:n_train], labels[:n_train]

    n_valid = cfg.BATCH_SIZE * int(cfg.VALIDATION_SPLIT * data.shape[0] / cfg.BATCH_SIZE)
    vdata, vlabels = data[-n_valid:], labels[-n_valid:]

    return (tdata, tlabels), (vdata, vlabels)

def load_best_model():
    """Return best model amongst models in predefined directory."""
    return _load_best_model(path_to_best_model())

def _load_best_model(dpath):
    """Return best model amongst models in <dpath>."""
    mdlpath = _path_to_best_model(dpath)
    if not mdlpath:
        log.critical("No best model fount at \"{0}\"".format(dpath))
        
    return load_model(mdlpath)    

def path_to_best_model():
    """Return path to best model amongst models in predefined directory."""
    return _path_to_best_model(tml.value('dnames', section='neuralnet', subkey='model'))

def _path_to_best_model(dpath):
    """Return path to best model amongst models in <dpath>."""
    fpaths = pth.__list_files(dpath)
    if not fpaths:
        log.error("\"{0}\" does not contain any file or is not a directory".format(dpath))
        return
    
    get_vloss = lambda fpath: float(pth.__no_extension(fpath).split('-')[-1])
    vlosses = list(map(get_vloss, fpaths))
    bmdl_idx = vlosses.index(min(vlosses))

    return fpaths[bmdl_idx]

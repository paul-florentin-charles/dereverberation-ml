# -*- coding: utf-8 -*-

import src.utils.logger as log
import src.parser.toml as tml
from src.datagen.utils import __pcm2float, __float2pcm


#TODO: Implement 2d-representation for data, to test a model with spectrum
    
def shape(data):
    log.debug("Shaping data")
    
    if data.ndim != 2:
        log.error("\'shape\' expects a two-dimensional array : (n_samples, sample_len)")
        return data

    _dtype = 'int{0}'.format(tml.value('audio', 'bit_depth'))
    
    if data.dtype != _dtype:
        log.warning("\'shape\' expects an {0} array".format(_dtype))
        
    data = data.astype('float64')
    for i in range(data.shape[0]):
        data[i] = __pcm2float(data[i].astype(_dtype))

    return data.reshape(*data.shape, 1)    

def unshape(data):
    log.debug("Unshaping data")
    
    if data.ndim != 3:
        log.error("\'unshape\' expects a two-dimensional array : (n_samples, sample_len, n_channels)")
        return data

    data = data.reshape(*data.shape[:-1])

    if data.dtype.kind != 'f':
        log.warning("\'unshape\' expects a float array")
        data = data.astype('float64')

    for i in range(data.shape[0]):
        data[i] = __float2pcm(data[i])

    return data.astype('int{0}'.format(tml.value('audio', 'bit_depth')))

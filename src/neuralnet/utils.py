# -*- coding: utf-8 -*-

import src.utils.logger as log
import src.parser.toml as tml
from src.datagen.utils import __pcm2float, __float2pcm


#TODO: Implement 2d-representation for data, to test a model with spectrum
    
def shape(data):
    if data.ndim != 2:
        log.error("\'shape\' expects a two-dimensional array : (n_samples, sample_len)")
        return data

    if data.dtype != 'int{0}'.format(tml.value('audio', 'bit_depth')):
        log.warning(''.join(["\'shape\' expects an ", DTYPE, " array"]))
        
    data = data.astype('float64')
    for i in range(data.shape[0]):
        data[i] = __pcm2float(data[i].astype(DTYPE))

    return data.reshape(*data.shape, 1)    

def unshape(data):
    if data.ndim != 3:
        log.error("\'unshape\' expects a two-dimensional array : (n_samples, sample_len, n_channels)")
        return data

    data = data.reshape(*data.shape[:-1])

    if data.dtype != 'float64':
        log.warning(''.join(["\'unshape\' expects a float64 array"]))
        data = data.astype('float64')

    for i in range(data.shape[0]):
        data[i] = __float2pcm(data[i])

    return data.astype('int{0}'.format(tml.value('audio', 'bit_depth')))

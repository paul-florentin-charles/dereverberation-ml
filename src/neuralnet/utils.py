# -*- coding: utf-8 -*-

import src.utils.logger as log


#TODO: Implement 2d-reprensation for data, to test a model with spectrum

def normalized(data):
    if data.ndim != 2:
        log.warning("\'normalize\' expects a two-dimensional array : (n_samples, sample_len)")
        return data
    
    data = data.astype('float64')
    for i in range(data.shape[0]):
        data[i] = data[i] / max(abs(data[i]))

    return data

def reshaped(data):
    if data.ndim != 2:
        log.error("\'reshape\' expects a two-dimensional array : (n_samples, sample_len)")
        return data
    
    return data.reshape(*data.shape, 1)


def shaped(data):
    return reshape(normalize(data))
    

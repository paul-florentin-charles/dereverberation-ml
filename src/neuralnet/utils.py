# -*- coding: utf-8 -*-

def normalize(data):
    data = data.astype('float64')
    data = data / max(map(max, data))

def reshape(data):
    return data.reshape(data.shape, -1)

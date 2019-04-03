# -*- coding: utf-8 -*-

# Normalize arrays using global maximum
def normalize(data):
    data = data.astype('float64')
    
    return data / max(map(max, data))

"""
# Normalize independently each array
def normalize(data):
    data = data.astype('float64')
    for i in range(data.shape[0]):
        data[i] = data[i] / max(data[i])

    return data
"""

def reshape(data):
    #return data.reshape(data.shape[0], 1, -1)
    return data.reshape(*data.shape, 1)


def shape(data):
    pass
    

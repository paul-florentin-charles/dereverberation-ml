# -*- coding: utf-8 -*-

import src.parser.toml as tml, src.parser.json as jsn
from src.datagen.utils import __mono, __convert
from src.datagen.io import _read, _load
import src.utils.logger as log

from random import choice
import numpy as np


def retrieve_data(preprocess=__mono):
    log.debug(''.join(['Retrieving data from \"', tml.value('json', 'fname'), '\"']))
    
    _dict = jsn.load()
    
    if not _dict:
        log.error(''.join(['No metadata found in ', tml.value('json', 'fname')]))

    data = []
    for key in _dict:
        data.append([__convert(choice(_load(_dict[key])), preprocess, _type=None), __convert(_read(key), preprocess, _type=None)])
    data = np.asarray(data)
    
    log.debug(''.join([str(data.shape[0]), ' couples data/label have been retrieved']))
    
    return data

# TODO: write data as npz directly when exporting data to gain time
def write_data(data):
    log.debug(''.join(['Writing data in \"', tml.value('data', 'fname'), '\"']))
    
    np.savez_compressed(tml.value('data', 'fname'), *data)

def read_data():
    log.debug(''.join(['Reading data from \"', tml.value('data', 'fname'), '\"']))

    data, labels = [np.zeros(tml.value('audio', 's_len'), dtype='int')] * 2

    _dict = np.load(tml.value('data', 'fname'))
    for fname in _dict:
        data = np.vstack((data, _dict[fname][0]))
        labels = np.vstack((labels, _dict[fname][1]))

    return np.delete(data, 0, 0), np.delete(labels, 0, 0)

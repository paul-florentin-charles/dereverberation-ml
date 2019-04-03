# -*- coding: utf-8 -*-

import src.parser.toml as tml, src.parser.json as jsn, src.parser.npz as npz
from src.datagen.utils import __convert
from src.datagen.io import _read, _load
import src.utils.logger as log

import numpy as np

from random import choice
from itertools import repeat


def retrieve_data():
    log.debug(''.join(["Retrieving data using \"", tml.value('json', 'fname'), "\""]))
    
    _dict = jsn.load()
    if not _dict:
        log.error(''.join([tml.value('json', 'fname'), " is empty"]))

    data = []
    for key in _dict:
        data.append(list(map(__convert, (choice(_load(_dict[key])), _read(key)), repeat(''.join(['int', str(tml.value('audio', 'bit_depth'))])))))
    
    log.debug(''.join([str(len(data)), ' couples data/label have been retrieved']))
    
    return np.asarray(data)

def write_data(data):
    npz.write(data)

def read_data():
    _dict = npz.read()
    
    data, labels = [np.zeros(tml.value('audio', 's_len'))] * 2
    for fname in _dict:
        data = np.vstack((data, _dict[fname][0]))
        labels = np.vstack((labels, _dict[fname][1]))

    return np.delete(data, 0, 0), np.delete(labels, 0, 0)

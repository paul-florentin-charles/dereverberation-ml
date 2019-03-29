# -*- coding: utf-8 -*-

import src.parser.toml as tml, src.parser.json as jsn
from src.datagen.utils import __mono, __convert
from src.datagen.io import _read, _load
import src.utils.logger as log

from random import choice
import numpy as np


# TODO: I could use asarray as well, idk
def retrieve_data(preprocess=__mono, _type=None):
    log.debug(''.join(["Retrieving data from ", tml.value('json', 'fname')]))
    
    _dict = jsn.load()

    if not _dict:
        log.error(''.join(["No metadata found in ", tml.value('json', 'fname')]))

    data, labels = [np.zeros(tml.value('audio', 's_len'), dtype='int')] * 2
    for key in _dict:
        data = np.vstack((data, __convert(choice(_load(_dict[key])), preprocess, _type)))
        labels = np.vstack((labels, __convert(_read(key), preprocess, _type)))
    
    return np.delete(data, 0, 0), np.delete(labels, 0, 0)

'''
def retrieve_data(preprocess=__mono, _type=None):
    log.debug(''.join(["Retrieving data from ", tml.value('json', 'fname')]))

    _dict = jsn.load()

    if not _dict:
        log.error(''.join(["No metadata found in ", tml.value('json', 'fname')]))

    data, labels = [] * 2
    for key in _dict:
        data.append(__convert(choice(_load(_dict[key])), preprocess, _type))
        labels.append(__convert(_read(key), preprocess, _type))
    
    return np.asarray(data), np.asarray(labels)

'''

# -*- coding: utf-8 -*-

import src.parser.toml as tml, src.parser.json as jsn
from src.datagen.utils import __mono, __convert
from src.datagen.io import _read, _load
import src.utils.logger as log
import src.utils.path as pth

from random import choice
import numpy as np


def retrieve_data(preprocess=__mono):
    log.debug(''.join(['Retrieving data from ', tml.value('json', 'fname')]))
    
    _dict = jsn.load()
    
    if not _dict:
        log.error(''.join(['No metadata found in ', tml.value('json', 'fname')]))

    data, labels = [np.zeros(tml.value('audio', 's_len'), dtype='int')] * 2
    for key in _dict:
        data = np.vstack((data, __convert(choice(_load(_dict[key])), preprocess, _type=None)))
        labels = np.vstack((labels, __convert(_read(key), preprocess, _type=None)))
    
    data, labels =  np.delete(data, 0, 0), np.delete(labels, 0, 0)
    log.debug(''.join([str(data.shape[0]), ' couples data/label have been retrieved']))
    
    return data, labels

# TODO: write data as npz directly when exporting data to gain time
def write_data(data, labels):
    log.debug(''.join(['Writing data in ', tml.value('neuralnet', 'fnames', 'input_data'), ' and ', tml.value('neuralnet', 'fnames', 'input_labels')]))
    
    if data.shape[0] != labels.shape[0]:
        log.critical("There are too many labels or too many data")

    if data.shape[1:] != labels.shape[1:]:
        log.error("Data and labels have different shapes")

    np.savez_compressed(tml.value('neuralnet', 'fnames', 'input_data'), *data)
    np.savez_compressed(tml.value('neuralnet', 'fnames', 'input_labels'), *labels)
    
def read_data():
    log.debug(''.join(['Reading data from ', tml.value('neuralnet', 'fnames', 'input_data'), ' and ', tml.value('neuralnet', 'fnames', 'input_labels')]))

    # Dicts are supposedly sorted
    data_dict, labels_dict = map(np.load, (tml.value('neuralnet', 'fnames', 'input_data') + '.npz', tml.value('neuralnet', 'fnames', 'input_labels') + '.npz'))

    data, labels = [np.zeros(tml.value('audio', 's_len'), dtype='int')] * 2

    for key in data_dict:
        data = np.vstack((data, data_dict[key]))

    for key in labels_dict:
        labels = np.vstack((labels, labels_dict[key]))

    return np.delete(data, 0, 0), np.delete(labels, 0, 0)

    

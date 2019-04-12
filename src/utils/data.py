# -*- coding: utf-8 -*-

import src.parser.toml as tml, src.parser.json as jsn, src.parser.npz as npz
import src.utils.logger as log
from src.datagen.utils import __convert
from src.datagen.io import _read, _load

import numpy as np

from itertools import repeat


DTYPE = 'int{0}'.format(tml.value('audio', 'bit_depth'))

def write_data():
    _dict = jsn.load()
    if not _dict:
        log.error("{0} is empty".format(tml.value('data', 'json', 'fname')))

    data = []
    for key in _dict:
        #TODO: Use choice to pick random extract instead of same reverb
        data.append(list(map(__convert, (_load(_dict[key])[0], _read(key)), repeat(DTYPE))))
    
    log.debug("{0} couples data/label have been retrieved".format(len(data)))

    npz.write(np.asarray(data))

def read_data():
    _dict = npz.read()
    
    data, labels = [np.zeros(tml.value('audio', 's_len'), dtype=DTYPE)] * 2
    for fname in _dict:
        data = np.vstack((data, _dict[fname][0]))
        labels = np.vstack((labels, _dict[fname][1]))

    return np.delete(data, 0, 0), np.delete(labels, 0, 0)

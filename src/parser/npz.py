# -*- coding: utf-8 -*-

import src.utils.logger as log
import src.utils.path as pth
import src.parser.toml as tml

import numpy as np


def write(data):
    _write(data, tml.value('data', 'fname'))

def read():
    return _read(tml.value('data', 'fname'))

def _write(data, fname):
    log.debug(''.join(['Writing data in \"', fname, '\"']))
    
    np.savez_compressed(fname, *data)

def _read(fname):
    log.debug(''.join(['Reading data from \"', fname, '\"']))

    if not pth.__is_file(fname):
        log.critical(''.join(["Numpy file ", fname, " not found, cannot read data"]))

    return np.load(fname)

# -*- coding: utf-8 -*-

import src.utils.logger as log
import src.utils.path as pth
import src.parser.toml as tml

import numpy as np


def write(data):
    _write(data, tml.value('data', 'numpy', 'fname'))

def read():
    return _read(tml.value('data', 'numpy', 'fname'))

def _write(data, fname):
    log.debug("Writing data in \"{0}\"".format(fname))
    
    np.savez_compressed(fname, *data)

def _read(fname):
    if not pth.__is_file(fname):
        log.critical("Numpy file \"{0}\" not found, cannot read data".format(fname))

    log.debug("Reading data from \"{0}\"".format(fname))

    return np.load(fname)

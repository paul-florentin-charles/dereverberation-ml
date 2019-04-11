# -*- coding: utf-8 -*-

import src.utils.logger as log
import src.utils.path as pth
import src.parser.toml as tml

import numpy as np


def write(data):
    """Write <data> into predefined numpy archive file."""
    _write(data, tml.value('data', 'numpy', 'fname'))

def read():
    """Read content of predefined numpy archive file."""
    return _read(tml.value('data', 'numpy', 'fname'))

def _write(data, fpath):
    """Write <data> into numpy archive file at <fpath>."""
    log.debug("Writing data in \"{0}\"".format(fpath))
    
    np.savez_compressed(fpath, *data)

def _read(fpath):
    """Read content of numpy archive file at <fpath>."""
    if not pth.__is_file(fpath):
        log.critical("Numpy file \"{0}\" not found, cannot read data".format(fpath))

    log.debug("Reading data from \"{0}\"".format(fpath))

    return np.load(fpath)

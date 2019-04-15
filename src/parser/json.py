# -*- coding: utf-8 -*-

import src.parser.toml as tml
import src.utils.path as pth
import src.utils.logger as log

import json


def init():
    """Initialize predefined json file."""
    dump(dict())

def dump(_dict, mode='w', n_indent=4):
    """Dump <_dict> into predefined json file."""
    _dump(tml.value('data', 'json','fname'), _dict, mode, n_indent)

def load():
    """Get content of predefined json file."""
    return _load(tml.value('data', 'json', 'fname'))

def _dump(fpath, _dict, mode='w', n_indent=4):
    """Dump <_dict> into json file at <fpath>.
    By default, mode is set to overwrite previous data.
    As well as an indentation is set for visualization purpose.
    """
    log.debug("Dumping data into \"{0}\"".format(fpath))

    fjson = pth.__open_file(fpath, _mode=mode)
    json.dump(_dict, fjson, indent=n_indent)
    pth.__close_file(fjson)

def _load(fpath):
    """Get content of json file at <fpath>."""
    if not pth.__is_file(fpath):
        log.critical("\"{0}\" doesn\'t exist, can\'t load data from it".format(fpath))

    log.debug("Loading data from \"{0}\"".format(fpath))

    fjson = pth.__open_file(fpath)
    ret = json.load(fjson)
    pth.__close_file(fjson)

    return ret

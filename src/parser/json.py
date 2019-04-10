# -*- coding: utf-8 -*-

import src.parser.toml as tml
import src.utils.path as pth
import src.utils.logger as log

import json


def init():
    pth.__create_file(tml.value('data', 'json', 'fname'))

def dump(_dict, mode='w', n_indent=4):
    _dump(tml.value('data', 'json','fname'), _dict, mode, n_indent)

def load():
    return _load(tml.value('data', 'json', 'fname'))

def _dump(fpath, _dict, mode='w', n_indent=4):
    log.debug("Dumping data into \"{0}\"".format(fpath))
    
    with open(fpath, mode) as fjson:
        json.dump(_dict, fjson, indent=n_indent)

def _load(fpath):
    if not pth.__is_file(fpath):
        log.critical("\"{0}\" doesn\'t exist, can\'t load data from it".format(fpath))

    log.debug("Loading data from \"{0}\"".format(fpath))
        
    with open(fpath, 'r') as fjson:
        return json.load(fjson) 

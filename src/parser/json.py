# -*- coding: utf-8 -*-

import src.parser.toml as tml
import src.utils.path as pth
import src.utils.logger as log

import json


def init():
    pth.__create_file(tml.value('json', 'fname'))

def dump(_dict, mode='w', n_ident=4):
    with open(tml.value('json','fname'), mode) as fjson:
        json.dump(_dict, fjson, indent=n_ident)

def load():
    json_fname = tml.value('json','fname')
    
    if not pth.__is_file(json_fname):
        log.critical(''.join([json_fname, ' doesn\'t exist, can\'t load data from it']))

    log.debug(''.join(["Loading data from \"", json_fname, "\""]))
    
    with open(json_fname, 'r') as fjson:
        return json.load(fjson)

def _dump(fpath, _dict, mode='w', n_ident=4):
    with open(fpath, mode) as fjson:
        json.dump(_dict, fjson, indent=n_ident)

def _load(fpath):
    with open(fpath, 'r') as fjson:
        return json.load(fjson) 

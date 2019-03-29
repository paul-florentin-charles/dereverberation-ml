# -*- coding: utf-8 -*-

import src.utils.logger as log
import src.utils.path as pth

import toml


CFG_FNAME = 'config.toml'

def value(section, key):
    if not pth.__is_file(CFG_FNAME):
        log.critical('Can\'t find config.toml at the root')
        
    return _value(CFG_FNAME, section, key)

def _value(fpath, section, key):
    _dict = toml.load(fpath)
    if section in _dict and key in _dict[section]:
        return _dict[section][key]
    
    return None

# -*- coding: utf-8 -*-

import toml


def _value(fpath, section, key):
    _dict = toml.load(fpath)
    if section in _dict and key in _dict[section]:
        return _dict[section][key]
    
    return None

def value(section, key):
    return _value('config.toml', section, key)

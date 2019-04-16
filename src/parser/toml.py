# -*- coding: utf-8 -*-

import src.utils.colors as clrs
from src.config import CFG_FNAME

import toml


def value(key, section=None, subkey=None):
    """Return specific value of config toml file.
    Config file name is defined in a global variable.
    """
    return _value(CFG_FNAME, key, section, subkey)

def _value(fpath, key, section=None, subkey=None):
    """Return specific value of a toml file at <fpath>.
    If <key> or <subkey> can't be found, return None.
    """
    _dict = toml.load(fpath)
    if not section:
        if key in _dict:
            return _dict[key]
        
        print(clrs.magenta("[ERROR] Unable to find \'{0}\', in *{1}*".format(key, fpath)))
        return None
    
    if section in _dict and key in _dict[section]:
        if not subkey:
            return _dict[section][key]
        elif subkey in _dict[section][key]:
            return _dict[section][key][subkey]
        
        print(clrs.magenta("[ERROR] Unable to find \'{0}\' in \'{1}\' in \'{2}\', in *{3}*".format(subkey, key, section, fpath)))
        return None

    print(clrs.magenta("[ERROR] Unable to find \'{0}\' in \'{1}\', in *{2}*".format(key, section, fpath)))
    return None

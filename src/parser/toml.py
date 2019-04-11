# -*- coding: utf-8 -*-

import src.utils.colors as clrs
from src.config import CFG_FNAME

import toml



def value(section, key, subkey=None):
    """Return specific value of config toml file.
    Config file name is defined in a global variable.
    """
    content = _value(CFG_FNAME, section, key, subkey)
    if content is None:
        if subkey:
            print(clrs.magenta("[ERROR] Unable to find \'{0}\' in \'{1}\' in \'{2}\'".format(subkey, key, section)))
        else:
            print(clrs.magenta("[ERROR] Unable to find \'{0}\' in \'{1}\'".format(key, section)))
    else:
        return content

def _value(fpath, section, key, subkey=None):
    """Return specific value of a toml file at <fpath>.
    If <key> or <subkey> can't be found, return None.
    """
    _dict = toml.load(fpath)
    if section in _dict and key in _dict[section]:
        if not subkey:
            return _dict[section][key]
        elif subkey in _dict[section][key]:
            return _dict[section][key][subkey]
        
    return None

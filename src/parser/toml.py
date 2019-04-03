# -*- coding: utf-8 -*-

# Cross-import doesn't work under python 3.5
#import src.utils.logger as log
import src.utils.colors as clrs
import src.utils.path as pth

import toml


CFG_FNAME = 'config.toml'

def value(section, key, subkey=None):
    if not pth.__is_file(CFG_FNAME):
        raise SystemExit(clrs._red_("[CRITICAL] Can\'t find config.toml at the root"))
        #log.critical('Can\'t find config.toml at the root')
        
    content = _value(CFG_FNAME, section, key, subkey)
    if content is None:
        print(clrs._magenta_(''.join(["[ERROR] Unable to find ", key, " in ", section])))
        #log.error(clrs._magenta_(''.join(["[ERROR] Unable to find ", key, " in ", section])))
    else:
        return content

def _value(fpath, section, key, subkey=None):
    _dict = toml.load(fpath)
    if section in _dict and key in _dict[section]:
        if not subkey:
            return _dict[section][key]
        elif subkey in _dict[section][key]:
            return _dict[section][key][subkey]
        
    return None

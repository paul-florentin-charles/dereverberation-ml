# -*- coding: utf-8 -*-

import src.parser.json as jsn
import src.utils.path as pth
import src.utils.logger as log
from src.datagen.utils import __list_audio_files

from itertools import repeat
from mimetypes import guess_type

"""A condition should be a function that takes a dictionary in input and return a boolean.

Example:

def is_bass(note_dict):
    return note_dict['instrument_family_str'] == 'bass'
"""

def filter_elements(dpath, cond_lst_lst):
    if not isinstance(cond_lst_lst, list) or not all(map(isinstance, cond_lst_lst, repeat(list))):
        log.critical("Please use a list of list of conditions to filter samples")

    jsnpaths = list(filter(__is_json_file, pth.__list_files(dpath)))
    if len(jsnpaths) != 1:
        log.critical("There should be exactly one json file at \"{0}\"".format(dpath))
    
    data = jsn._load(jsnpaths[0])
    audio_fnames = __list_audio_files(dpath)
    
    for afile in audio_fnames:
        if not all(map(lambda cond_lst: any(map(lambda cond: cond(data[pth.__no_extension(afile)]), cond_lst)), cond_lst_lst)):
            pth.__remove_file(afile)

def __is_json_file(fpath):
    """Return True if <fpath> is a json file.
    Otherwise return False.
    """
    if not pth.__is_file(fpath):
        return False

    info = guess_type(fpath)[0]
    
    return info.split('/')[1] == 'json'

# Conditions

## Instrument

def is_bass(note_dict):
    return note_dict['instrument_family_str'] == 'bass'

def is_brass(note_dict):
    return note_dict['instrument_family_str'] == 'brass'

def is_flute(note_dict):
    return note_dict['instrument_family_str'] == 'flute'

def is_guitar(note_dict):
    return note_dict['instrument_family_str'] == 'guitar'

def is_keyboard(note_dict):
    return note_dict['instrument_family_str'] == 'keyboard'

def is_mallet(note_dict):
    return note_dict['instrument_family_str'] == 'mallet'

def is_organ(note_dict):
    return note_dict['instrument_family_str'] == 'organ'

def is_reed(note_dict):
    return note_dict['instrument_family_str'] == 'reed'

def is_string(note_dict):
    return note_dict['instrument_family_str'] == 'string'

def is_synth_lead(note_dict):
    return note_dict['instrument_family_str'] == 'synth_lead'

def is_vocal(note_dict):
    return note_dict['instrument_family_str'] == 'vocal'

## Source

def is_acoustic(note_dict):
    return note_dict['instrument_source_str'] == 'acoustic'

def is_electronic(note_dict):
    return note_dict['instrument_source_str'] == 'electronic'

def is_synthetic(note_dict):
    return note_dict['instrument_source_str'] == 'synthetic'

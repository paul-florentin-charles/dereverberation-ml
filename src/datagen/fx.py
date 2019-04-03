# -*- coding: utf-8 -*-

"""
Apply fx to a dry sound
"""

import src.datagen.utils as utls
import src.parser.toml as tml
import src.utils.logger as log

from scipy.signal import convolve

from itertools import repeat


def _convolve(dry, fx):
    _mode = tml.value('audio', 'conv_mod')
    if _mode not in ['full', 'same', 'valid']:
        log.critical(''.join(['\"', _mode, '\": unrecognized convolution mode']))
    
    dry, fx = map(utls.__with_sample_rate, (dry, fx), repeat(tml.value('audio', 's_rate')))
    
    if tml.value('audio', 'mono'):
        dry, fx = map(utls.__mono, (dry, fx))
        _dry, _fx = map(utls.__convert, (dry, fx), repeat(''.join(['int', str(tml.value('audio', 'bit_depth'))]))) 
        _dry, _fx = map(utls.__pcm2float, (_dry, _fx))
    else:
        log.critical("Stereo not implemented, please set 'mono' to true in \"config.toml\"")

    _conv = convolve(_dry, _fx, mode=_mode)
    _conv = utls.__normalize(_conv)
    _conv = utls.__float2pcm(_conv)
    
    return _conv

def _apply_fxs(dry, fxs, func=_convolve):
    wet_signals = []
    
    if dry.frame_count() == 0:
        log.warning("Attempting to apply fx to an empty signal")
        return wet_signals
    
    for fx in fxs:
        wet_signals.append(func(dry, fx))
    
    return wet_signals

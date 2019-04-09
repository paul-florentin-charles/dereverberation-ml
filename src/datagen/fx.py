# -*- coding: utf-8 -*-

"""
Apply fx to a dry sound
"""

import src.datagen.utils as utls
import src.parser.toml as tml
import src.utils.logger as log
from src.utils.tools import n_parameters

import scipy.signal as sig

from itertools import repeat


# TODO: Stereo not implemented, mono signals automatically converted to mono
def convolve(dry, fx):
    mode = tml.value('audio', 'conv_mod')
    sr = tml.value('audio', 's_rate')
    bits = tml.value('audio', 'bit_depth')
    
    dry, fx = map(utls.__with_sample_rate, (dry, fx), repeat(sr))
    dry, fx = map(utls.__with_bit_depth, (dry, fx), repeat(bits))
    dry, fx = map(utls.__mono, (dry, fx))
        
    sigs = tuple(map(utls.__convert, (dry, fx), repeat('int{0}'.format(bits))))

    return _convolve(*sigs, mode)

def _convolve(npy_dry, npy_fx, _mode):
    npy_dry, npy_fx = map(utls.__pcm2float, (npy_dry, npy_fx))

    _conv = sig.convolve(npy_dry, npy_fx, mode=_mode)
    _conv = utls.__normalize(_conv)
    _conv = utls.__float2pcm(_conv)
    
    return _conv

def _apply_fxs(dry, fxs, func=convolve):
    wet_signals = []
    
    n_params = n_parameters(func)
    if n_params == -1:
        log.critical("A function is needed to apply fxs")
    elif n_params != 2:
        log.critical(''.join(['\'',func.__name__, "\' function doesn't take exactly two arguments, can't apply fxs"]))
    
    if dry.frame_count() == 0:
        log.warning("Attempting to apply fx to an empty signal")
        return wet_signals
    
    for fx in fxs:
        wet_signals.append(func(dry, fx))
    
    return wet_signals

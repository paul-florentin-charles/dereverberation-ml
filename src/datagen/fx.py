# -*- coding: utf-8 -*-

"""Tools to apply fxs to a sound."""

import src.datagen.utils as utls
import src.parser.toml as tml
import src.utils.logger as log
from src.utils.tools import n_parameters

import scipy.signal as sig

from itertools import repeat


# TODO: Stereo not implemented, mono signals automatically converted to mono
def convolve(dry, fx):
    """Convolve two audio segments together.
    Return a numpy array of integers.
    """
    mode = tml.value('conv_mod', section='audio')
    sr = tml.value('s_rate', section='audio')
    bits = tml.value('bit_depth', section='audio')
    
    dry, fx = map(utls.__with_sample_rate, (dry, fx), repeat(sr))
    dry, fx = map(utls.__with_bit_depth, (dry, fx), repeat(bits))
    dry, fx = map(utls.__mono, (dry, fx))
    
    sigs = map(utls.__convert, (dry, fx), repeat('int{0}'.format(bits)))

    return _convolve(*sigs, mode)

def apply_fx(dry, fx, func=convolve):
    """Apply an fx to a dry signal.
    Return the resulting signal.
    """
    if func is None:
        func = convolve
    
    n_params = n_parameters(func)
    if n_params == -1:
        log.critical("A function is needed to apply fx")
    elif n_params != 2:
        log.critical("\'{0}\' function doesn't take exactly two arguments, can't apply fx".format(func.__name__))
    
    if dry.frame_count() == 0:
        log.warning("Applying fx to an empty signal")
    
    return func(dry, fx)

def _convolve(npy_dry, npy_fx, _mode):
    """Compute convolution between two arrays.
    Arrays are supposed numpy arrays of integers.
    """
    npy_dry, npy_fx = map(utls.__pcm2float, (npy_dry, npy_fx))

    _conv = sig.convolve(npy_dry, npy_fx, mode=_mode)
    _conv = utls.__normalize(_conv)
    _conv = utls.__float2pcm(_conv)
    
    return _conv

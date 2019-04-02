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
    
    dry, fx = map(utls.__set_sample_rate, (dry, fx), repeat(tml.value('audio', 's_rate')))
    
    if utls.__is_mono(dry) or utls.__is_mono(fx):
        _dry, _fx = utls.__convert(dry, utls.__mono, 'int16'), utls.__convert(fx, utls.__mono, 'int16')
        _dry, _fx = utls.__pcm2float(_dry), utls.__pcm2float(_fx)
    else:
        _dry, _fx = utls.__convert(dry), utls.__convert(fx)
        _dry, _fx = utls.__normalize(_dry, sum), utls.__normalize(_fx, sum)

    _conv = convolve(_dry, _fx, mode=_mode)
    _conv = utls.__normalize(_conv, sum) if _conv.ndim == 2 else utls.__normalize(_conv)
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

# -*- coding: utf-8 -*-

"""Set and get audio properties"""

import src.utils.path as pth
import src.utils.logger as log

import numpy as np
import fleep


## Useful to avoid picking non audio files ##
"""
from mimetypes import guess_type

def __is_audio_file(fpath):
    \"""Return True if <fpath> is an audio file.
    Otherwise return False.
    \"""
    if not pth.__is_file(fpath):
        return False

    info = guess_type(fpath)[0]
    
    return info.split('/')[0] == 'audio'
"""
def __is_audio_file(fpath):
    """Return True if <fpath> is an audio file.
    Otherwise return False.
    """
    if not pth.__is_file(fpath):
        return False

    f = pth.__open_file(fpath, _mode='rb')
    info = fleep.get(f.read(128))
    pth.__close_file(f)
    
    return info.type_matches('audio')

def __list_audio_files(path, recursively=True):
    """Return a list of audio files at <path>.
    If <recursively> is set to True, look for files recursively in-depth.
    """
    return list(filter(__is_audio_file, pth.__list_files(path, recursively)))

## Various functions based on audio properties ##
              
def __mono(audio_segment):
    """Return a mono version of <audio_segment>."""
    return audio_segment.set_channels(1)

def __with_sample_rate(audio_segment, sample_rate):
    """Return a version of <audio_segment> with updated sample rate."""
    return audio_segment.set_frame_rate(sample_rate)

def __with_bit_depth(audio_segment, bit_depth):
    """Return a version of <audio_segment> with updated bit depth."""
    if bit_depth % 8 != 0:
        log.error("Bit depth should be a multiple of 8, used value here is {0}".format(bit_depth))
        
    return audio_segment.set_sample_width(bit_depth // 8)

def __convert(audio_segment, _type=None):
    """Convert <audio_segment> into numpy array with dtype <_type>.
    If <_type> is None, by default 'float64' dtype is used.
    """
    return np.array(audio_segment.get_array_of_samples(), dtype=_type)

def __normalize(npy_array):
    """Normalize <npy_array> by its maximum in absolute value.
    If maximum is null, return the same array.
    """
    M = max(abs(npy_array))
    if M:
        return npy_array / M
    
    return npy_array

def __float2pcm(npy_array, _type='int16'):
    """Convert <npy_array> from float to pcm.
    Default conversion type is 'int16'.
    """
    info = np.iinfo(_type)
    amp = 2**(info.bits - 1)
    offset = info.min + amp
    
    npy_array = npy_array * amp + offset

    return npy_array.clip(info.min, info.max).astype(_type)

def __pcm2float(npy_array, _type='float64'):
    """Convert <npy_array> from pcm to float.
    Default conversion type is 'float64'.
    """
    if npy_array.dtype.kind != 'i':
        log.error("\'__pcm2float\' takes an array of integers, forcing conversion to int16")
        npy_array = npy_array.astype('int16')
        
    info = np.iinfo(npy_array.dtype)
    amp = 2**(info.bits - 1)
    offset = info.min + amp
    
    npy_array = (npy_array - offset) / amp

    return npy_array.clip(-1., 1.).astype(_type)

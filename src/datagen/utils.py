# -*- coding: utf-8 -*-

"""
Set and get audio properties
"""

import src.utils.path as pth

import numpy as np
import fleep


## Useful to avoid picking non audio files ##

def __is_audio_file(fpath):
    """Returns True if <fpath> is an audio file
    Otherwise returns False
    """
    if not pth.__is_file(fpath):
        return False

    with pth._path(fpath).open(mode='rb') as f:
        info = fleep.get(f.read(128))
        return info.type_matches('audio')

    return False

def __list_audio_files(path, recursively=True):
    """Lists audio files at <path>
    If <recursively> is set to True, listing is recursive
    """
    return list(filter(__is_audio_file, pth.__list_files(path, recursively)))

## Various functions based on audio properties ##
              
def __mono(audio_segment):
    """Returns a mono version of <audio_segment>"""
    return audio_segment.set_channels(1)

def __with_sample_rate(audio_segment, sample_rate):
    """Returns a version of <audio_segment> with updated sample rate"""
    return audio_segment.set_frame_rate(sample_rate)

def __with_bit_depth(audio_segment, bit_depth):
    """Returns a version of <audio_segment> with updated bit depth"""
    return audio_segment.set_sample_width(bit_depth // 8)

def __convert(audio_segment, _type=None):
    """Converts <audio_segment> into numpy array with dtype <_type>"""
    return np.array(audio_segment.get_array_of_samples(), dtype=_type)

def __normalize(npy_array):
    """Normalizes <npy_array> by its maximum"""
    return npy_array / max(npy_array)

def __float2pcm(npy_array, _type='int16'):    
    info = np.iinfo(_type)
    amp = 2**(info.bits - 1)
    offset = info.min + amp
    
    npy_array = npy_array * amp + offset

    return npy_array.clip(info.min, info.max).astype(_type)

def __pcm2float(npy_array, _type='float64'):    
    info = np.iinfo(npy_array.dtype)
    amp = 2**(info.bits - 1)
    offset = info.min + amp
    
    npy_array = (npy_array - offset) / amp

    return npy_array.clip(-1., 1.).astype(_type)

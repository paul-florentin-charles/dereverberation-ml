# -*- coding: utf-8 -*-

"""Load any sound file, and save numpy arrays as wave files."""

from src.datagen.utils import __list_audio_files, __is_audio_file
from src.datagen.fx import apply_fxs
from src.utils.tools import mkrdir, rstr
import src.utils.logger as log
import src.utils.path as pth
import src.parser.toml as tml, src.parser.json as jsn

from pydub import AudioSegment
from scipy.io.wavfile import write


## Reading and writing audio files ##

def _read(fpath):
    """Read sound at <fpath> as a pydub AudioSegment."""
    if __is_audio_file(fpath):
        return AudioSegment.from_file(pth.__path(fpath))

    log.warning("{0} is not an audio file".format(fpath))
    
    return AudioSegment.empty()

def _load(dpath):
    """Read all sounds at <dpath> in a list of pydub AudioSegment."""
    audio_segments = []
    for fpath in pth.__list_files(dpath):
        if __is_audio_file(fpath):
            audio_segments.append(_read(fpath))

    if len(audio_segments) == 0:
        log.warning("{0} does not contain any audio file".format(dpath))
        
    return audio_segments

def _save(npy_array, fpath, override=True):
    """Save a numpy array as a wave file at <fpath>."""
    if not override and pth.__exists(fpath):
        return
    
    while pth.__file_name(fpath).endswith('.'):
        fpath = pth.__with_name(fpath, pth.__file_name(fpath)[:-1])
    
    if pth.__file_extension(fpath) != '.wav':
        fpath = pth.__with_extension(fpath, '.wav')

    write(fpath, tml.value('audio', 's_rate'), npy_array)

def _export(npy_arrays, outdpath=None, override=True):
    """Save a list of numpy arrays as wave files at <outdpath>.
    If <outdpath> is None, creates a random directory.
    """
    if outdpath is None:
        outdpath = mkrdir()

    for idx, npy_array in enumerate(npy_arrays):
        _save(npy_array, pth.__join_path(outdpath, '{0}_{1}'.format(idx, rstr())), override)

## Generating dataset ##

def generate_dataset(dry_dpath, fx_dpath, output_dir=None, func=None):
    """Generate dataset of wet samples."""
    if not output_dir:
        output_dir = mkrdir()
    elif not pth.__exists(output_dir):
        pth.__make_dir(output_dir)

    fxs = _load(fx_dpath)

    jsn.init()

    info = dict()
    
    for idx, dryfpath in enumerate(__list_audio_files(dry_dpath)):
        wet_signals = apply_fxs(_read(dryfpath), fxs, func)
        dpath = mkrdir(output_dir, prefix='{0}_'.format(idx))
        _export(wet_signals, dpath)

        info[dryfpath] = dpath
        if (idx + 1) % tml.value('data', 'save_steps') == 0:
            log.debug("{0} samples processed".format(idx + 1))
            jsn.dump(info)

    jsn.dump(info)

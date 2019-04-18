# -*- coding: utf-8 -*-

"""Wrapper around built-in python library 'pathlib'."""

from src.utils.decorators import stringify

from pathlib import Path
from io import TextIOWrapper as IO


def pathify(func):
    def wrapper(*args, **kwargs):
        if len(args) == 0:
            return func(*args, **kwargs)
        return func(Path(args[0]), *args[1:], **kwargs)

    return wrapper

## path ##

@pathify
@stringify
def __path(fpath):
    return fpath

@stringify
def __current_dir():
    return Path.cwd()

## path segmentation ##

@pathify
@stringify
def __file_extension(fpath):
    return fpath.suffix

# Doesn't work if multiple dots (e.g. tar.gz files)
@pathify
@stringify
def __no_extension(fpath):
    return fpath.stem

@pathify
@stringify
def __file_name(fpath):
    return fpath.name

@pathify
@stringify
def __parent_path(fpath):
    return fpath.parent

## path modification ##

@pathify
@stringify
def __join_path(lpath, rpath):
    return lpath.joinpath(rpath)

@pathify
@stringify
def __with_name(fpath, fname):
    return fpath.with_name(fname)

@pathify
@stringify
def __with_extension(fpath, fextension):
    return fpath.with_suffix(fextension)

## path booleans ##

@pathify
def __exists(path):
    return path.exists()

@pathify
def __is_file(path):
    return path.is_file()

@pathify
def __is_dir(path):
    return path.is_dir()

@pathify
def __is_empty(path):
    if __is_dir(path):
        return len(__list_files(path)) == 0
    return True

## file/dir manipulation ##

@pathify
def __make_dir(path):
    if not __exists(path):
        path.mkdir()

@pathify
def __remove_dir(path):
    if __is_dir(path):
        path.rmdir()
        
@pathify        
def __create_file(path, override=True):
    if not __is_dir(path):
        path.touch(exist_ok=override)

@pathify
def __remove_file(path):
    if __is_file(path):
        path.unlink()

@pathify
def __open_file(path, _mode='r'):
    if not __is_dir(path):
        return path.open(mode=_mode)

def __close_file(f):
    if isinstance(f, IO):
        f.close()

@pathify
def __write_file(path, data):
    if not __is_dir(path):
        path.write_bytes(data)

@pathify
def __read_file(path):
    if __is_file(path):
        return path.read_text()

@pathify
def __rename_file(src_path, dst_path):
    if __is_file(src_path):
        src_path.rename(dst_path)
    
## miscellaneous ##

@pathify
@stringify
def __list_files(path, recursively=True):
    if __is_file(path):
        return [path]
    elif __is_dir(path):
        return list(filter(__is_file, path.glob('**/*') if recursively else path.iterdir()))
    return []

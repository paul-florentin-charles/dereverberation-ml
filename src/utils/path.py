# -*- coding: utf-8 -*-

"""Wrapper around built-in python library 'pathlib'."""

from pathlib import Path


def stringify(func):
    """Decorator to convert function output to string or to a list of strings."""
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, list):
            return map(str, res)
        else:
            return str(res)
    
    return wrapper

## path ##

def _path(fpath):
    return Path(fpath)

@stringify
def __path(fpath):
    return Path(fpath)

## path segmentation ##

@stringify
def __file_extension(fpath):
    return _path(fpath).suffix

# Doesn't work if multiple dots (e.g. tar.gz files)
@stringify
def __no_extension(fpath):
    return _path(fpath).stem

@stringify
def __file_name(fpath):
    return _path(fpath).name

@stringify
def __parent_path(fpath):
    return _path(fpath).parent

## path modification ##

@stringify
def __join_path(lpath, rpath):
    return _path(lpath).joinpath(_path(rpath))

@stringify
def __with_name(fpath, fname):
    return _path(fpath).with_name(fname)

@stringify
def __with_extension(fpath, fextension):
    return _path(fpath).with_suffix(fextension)

## path booleans ##

def __exists(path):
    return _path(path).exists()

def __is_file(path):
    return _path(path).is_file()

def __is_dir(path):
    return _path(path).is_dir()

## file/dir manipulation ##

def __make_dir(path):
    if not __exists(path):
        _path(path).mkdir()

def __remove_dir(path):
    if __is_dir(path):
        _path(path).rmdir()
    
def __create_file(path, override=True):
    if not __is_dir(path):
        _path(path).touch(exist_ok=override)
    
def __remove_file(path):
    if __is_file(path):
        _path(path).unlink()

def __write_file(path, data):
    if not __is_dir(path):
        _path(path).write_bytes(data)

## miscellaneous ##

@stringify
def __list_files(path, recursively=True):
    if __is_file(path):
        return [path]
    elif __is_dir(path):
        if recursively:
            return list(filter(__is_file, _path(path).glob('**/*')))
        else:
            return list(filter(__is_file, _path(path).iterdir()))
    return []

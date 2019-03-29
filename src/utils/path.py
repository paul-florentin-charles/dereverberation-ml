# -*- coding: utf-8 -*-

"""
Layer to use already very simple library *pathlib*
"""

from pathlib import Path


def __path(fpath):
    return Path(fpath)

## path segmentation ##

def __file_extension(fpath):
    return __path(fpath).suffix

# Doesn't work if multiple dots (e.g. tar.gz files)
def __no_extension(fpath):
    return __path(fpath).stem

def __file_name(fpath):
    return __path(fpath).name

def __parent_path(fpath):
    return __path(fpath).parent

## path modification ##

def __join_path(lpath, rpath):
    return __path(lpath).joinpath(__path(rpath))

def __with_name(fpath, fname):
    return __path(fpath).with_name(fname)

def __with_extension(fpath, fextension):
    return __path(fpath).with_suffix(fextension)

## path booleans ##

def __exists(path):
    return __path(path).exists()

def __is_file(path):
    return __path(path).is_file()

def __is_dir(path):
    return __path(path).is_dir()

## file/dir manipulation ##

def __make_dir(path):
    if not __exists(path):
        __path(path).mkdir()

def __remove_dir(path):
    if __is_dir(path):
        __path(path).rmdir()
    
def __create_file(path, override=True):
    if not __is_dir(path):
        __path(path).touch(exist_ok=override)
    
def __remove_file(path):
    if __is_file(path):
        __path(path).unlink()

def __write_file(path, data):
    if not __is_dir(path):
        __path(path).write_bytes(data)

## miscellaneous ##

def __list_files(path, recursively=True):
    if __is_file(path):
        return [path]
    elif __is_dir(path):
        if recursively:
            return list(filter(__is_file, __path(path).glob('**/*')))
        else:
            return list(filter(__is_file, __path(path).iterdir()))
    return []

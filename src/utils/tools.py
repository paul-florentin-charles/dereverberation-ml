# -*- coding: utf-8 -*-

"""Set of useful functions that don't belong to a specific module.

Typically used for downloading, extracting archive or printing program usage.
"""

import src.utils.colors as clrs
import src.utils.path as pth
import src.utils.logger as log

from random import choice
from string import ascii_letters, digits
from shutil import unpack_archive
import requests as req
from http import HTTPStatus as HTTP
from inspect import signature, currentframe


def usage(pname, cname='python3', required_args=[], optional_args=[]):
    """Generic usage function for a program.
    Return a printable string.
    """
    return 'Usage: {0} {1} {2} {3}'.format(clrs.magenta(cname), clrs.cyan(pname), ' '.join(required_args), ' '.join(map(lambda arg: '[{0}]'.format(arg), optional_args)))

def rstr(lth=4, chrs=''.join([ascii_letters, digits])):
    """Generate a random string of size <lth> containing chars picked in <chrs>."""
    return ''.join(choice(chrs) for _ in range(lth))

def mkrdir(path='.', prefix=''):
    """Create a random directory at <path>, prefixed by <prefix>.
    Return path to created directory.
    """
    dpath = pth.__join_path(path, ''.join([prefix, rstr()]))
    while(pth.__exists(dpath)):
        dpath = pth.__join_path(path, ''.join([prefix, rstr()]))
    pth.__make_dir(dpath)

    return dpath

def download(furl, dpath='.'):
    """Download file at <furl> and write it at <dpath>.
    Return path to extracted file.
    """
    log.debug("Downloading file from \"{0}\" into \"{1}\"".format(furl, dpath))

    response = req.get(furl)
    if response.status_code != req.codes.ok:
        if response.status_code == HTTP.NOT_FOUND:
            log.critical(''.join(['File not found at: ', furl]))
        else:
            log.critical(''.join(['Error code: ', response.status_code,', getting: ', furl]))
    
    fpath = pth.__join_path(dpath, pth.__file_name(furl))
    pth.__write_file(fpath, response.content)

    return fpath

def extract(fpath, dpath):
    """Extract archive at <fpath> into <dpath>."""
    log.debug("Extracting \"{0}\" into \"{1}\"".format(fpath, dpath))

    try:
        unpack_archive(fpath, dpath)
    except ValueError:
        log.critical("\"{0}\" not a valid archive".format(fpath))
        
    pth.__remove_file(fpath)

def n_parameters(func):
    """Return number of parameters of <func> if it's a function.
    Otherwise return -1.
    """
    if not callable(func):
        log.warning("\'{0}\' is not a function".format(func))
        return -1
    
    return len(signature(func).parameters)
    

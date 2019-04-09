# -*- coding: utf-8 -*-

import src.utils.colors as clrs
import src.utils.path as pth
import src.utils.logger as log

from random import choice
from shutil import unpack_archive
from string import ascii_letters, digits
import requests as req
from http import HTTPStatus as HTTP
from inspect import signature


def usage(pname, cname='python3', required_args=[], optional_args=[]):
    '''Generic usage function that returns a string'''
    return 'Usage: {0} {1} {2} {3}'.format(clrs._magenta_(cname), clrs._cyan_(pname), ' '.join(required_args), ' '.join(map(lambda x : '[{0}]'.format(x), optional_args)))

def rstr(lth=4, chrs=''.join([ascii_letters, digits])):
    '''Generates a random string of size <lth> containing chars picked in <chrs>'''
    return ''.join(choice(chrs) for _ in range(lth))

def mkrdir(path='.', prefix=''):
    """Creates a random directory at <path>, prefixed by <prefix>.
    Returns path to created directory
    """
    dpath = pth.__join_path(path, ''.join([prefix, rstr()]))
    while(pth.__exists(dpath)):
        dpath = pth.__join_path(path, ''.join([prefix, rstr()]))
    pth.__make_dir(dpath)

    return dpath

def download(furl, dpath='.'):
    """Download file at <furl> and write it at <dpath>
    Returns path to extracted file
    """
    log.debug(''.join(["Downloading file from \"", furl, "\" into \"", dpath, "\""]))

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
    """Extracting archive at <fpath> into <dpath>"""
    log.debug(''.join(['Extracting \"', str(fpath), '\" into \"', str(dpath), '\"']))

    try:
        unpack_archive(fpath, dpath)
    except ValueError:
        log.critical(''.join(['\"', fpath, '\" not a valid archive']))
        
    pth.__remove_file(fpath)

def n_parameters(func):
    """Returns number of parameters if <func> is a function
    Otherwise returns -1
    """
    if not callable(func):
        log.warning(''.join([str(func), " is not a function"]))
        return -1
    
    return len(signature(func).parameters)

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


def usage(pname, required_args = [], optional_args = []):
    '''Generic usage function that returns a string'''
    return ''.join([clrs._bright_('Usage:'), clrs._magenta_(' python3 '), clrs._cyan_(pname), ' ', ' '.join(required_args), ' ', ' '.join([''.join(['[', arg, ']']) for arg in optional_args])])

def rstr(lth=4, chrs=''.join([ascii_letters, digits])):
    '''Generates a random string of size <lth> containing chars picked in <chrs>'''
    return ''.join(choice(chrs) for _ in range(lth))

def mkrdir(path='.', prefix=''):
    dpath = pth.__join_path(path, ''.join([prefix, rstr()]))
    while(pth.__exists(dpath)):
        dpath = pth.__join_path(path, ''.join([prefix, rstr()]))
    pth.__make_dir(dpath)

    return dpath

def download(furl):
    log.debug(''.join(['Downloading file from \"', furl, '\"']))

    response = req.get(furl)
    if response.status_code != req.codes.ok:
        if response.status_code == HTTP.NOT_FOUND:
            log.critical(''.join(['File not found at: ', furl]))
        else:
            log.critical(''.join(['Error code: ', response.status_code,', getting: ', furl]))
    
    fname = pth.__file_name(furl)
    pth.__write_file(fname, response.content)

    return fname

def extract(fname, dname):
    log.debug(''.join(['Extracting \"', fname, '\" into \"', dname, '\"']))

    try:
        unpack_archive(fname, dname)
    except ValueError:
        log.critical(''.join(['\"', fname, '\" not a valid archive']))
        
    pth.__remove_file(fname)

def n_parameters(func):
    if not callable(func):
        log.warning(''.join([str(func), " is not a function"]))
        return -1
    
    return len(signature(func).parameters)

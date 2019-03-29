# -*- coding: utf-8 -*-

import src.utils.colors as clrs
import src.utils.path as pth
import src.utils.logger as log

from random import choice
from shutil import unpack_archive
from string import ascii_letters, digits
import requests as req


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
    log.debug(''.join(['Downloading file from ', furl]))

    content = req.get(furl).content
    
    fname = pth.__file_name(furl)
    pth.__write_file(fname, content)

    return fname

def extract(fname, dname):
    log.debug(''.join(['Extracting ', fname, ' into ', dname]))
    
    unpack_archive(fname, dname)
    pth.__remove_file(fname)

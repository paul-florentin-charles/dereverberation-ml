#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.check_version import check_version

check_version()


import src.utils.path as pth
import src.parser.toml as tml

from shutil import rmtree


def clean():
    dnames = tml.value('demo', 'dnames')
    if pth.__exists(dnames['input_dry']):
        rmtree(dnames['input_dry'])
    if pth.__exists(dnames['input_fx']):
        rmtree(dnames['input_fx'])
    if pth.__exists(dnames['output']):
        rmtree(dnames['output'])

    pth.__remove_file(tml.value('json', 'fname'))

    fnames = tml.value('data', 'fnames')
    pth.__remove_file(fnames['input_data'])
    pth.__remove_file(fnames['input_labels'])

    
if __name__ == '__main__':
    if __file__.replace('./', '') != "clean.py":
        raise SystemExit("Please execute script from its directory")
    
    clean()

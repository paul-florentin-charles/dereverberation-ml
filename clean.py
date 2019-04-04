#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.check import check

check()


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

    pth.__remove_file(tml.value('data', 'json', 'fname'))
    pth.__remove_file(tml.value('data', 'numpy', 'fname'))

    
if __name__ == '__main__':
    if __file__.replace('./', '') != "clean.py":
        raise SystemExit("Please execute script from its directory")
    
    clean()

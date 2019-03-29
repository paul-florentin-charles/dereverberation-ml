#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import src.utils.path as pth
import src.utils.logger as log
import src.parser.toml as tml
from src.utils.tools import download, extract
from src.run import run

import requests as req
from shutil import unpack_archive

    
def demo():
    log.init()
    
    # Downloading data from URLs

    base_url = tml.value('demo', 'datasets_url')

    size = tml.value('demo', 'size')
    if size not in ['tiny', 'small', 'medium', 'big']:
        log.error(''.join(['\"', size, '\": unrecognized demo size']))

    note_url = ''.join([base_url, 'note_dataset_', size, '.tar.gz'])
    fx_url = ''.join([base_url, 'ir_dataset_', size, '.zip'])

    log.info('Downloading datasets of notes and impulse responses')

    note_fname, fx_fname = download(note_url), download(fx_url)

    # Extracting data

    dnames = tml.value('demo', 'dnames')

    extract(note_fname, dnames[0])
    extract(fx_fname, dnames[1])

    # Execute main script

    run(*dnames)

    log.shutdown()


if __name__ == '__main__':
    if __file__.replace('./', '') != "demo.py":
        raise SystemExit("Please execute script from its directory")
    
    demo()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.check_version import check_version

check_version()


import src.utils.logger as log
import src.utils.path as pth
import src.parser.toml as tml
from src.utils.tools import download, extract

from src.run import run

    
def demo():
    log.init()
    
    # Downloading data from URLs and extracting downloaded files

    base_url = tml.value('demo', 'datasets_url')

    size = tml.value('demo', 'size')
    if size not in ['tiny', 'small', 'medium', 'big']:
        log.error(''.join(['\"', size, '\": unrecognized demo size']))

    note_url = ''.join([base_url, 'note_dataset_', size, '.tar.gz'])
    fx_url = ''.join([base_url, 'ir_dataset_', size, '.zip'])

    dry_dpath = tml.value('demo', 'dnames', 'input_dry')
    fx_dpath = tml.value('demo', 'dnames', 'input_fx')

    if not pth.__exists(dry_dpath) and not pth.__exists(fx_dpath):
        log.info("Downloading datasets of notes and impulse responses")
        
        note_fname, fx_fname = download(note_url), download(fx_url)

        log.info('Extracting datasets')
        
        extract(note_fname, dry_dpath)
        extract(fx_fname, fx_dpath)
    elif not pth.__exists(dry_dpath) and pth.__exists(fx_dpath):
        log.info("Downloading dataset of notes")
        
        note_fname = download(note_url)

        log.info('Extracting dataset of notes')
        
        extract(note_fname, dry_dpath)
    elif pth.__exists(dry_dpath) and not pth.__exists(fx_dpath):
        log.info("Downloading dataset of impulse responses")
        
        fx_fname = download(fx_url)

        log.info('Extracting dataset of impulse responses')
        
        extract(fx_fname, fx_dpath)
    else:
        log.info("Skipping downloading since directories are still here, remove them if you wish to download new datasets")

    # Executing main script

    run(dry_dpath, fx_dpath, tml.value('demo', 'dnames', 'output'))

    log.shutdown()


if __name__ == '__main__':
    if __file__.replace('./', '') != "demo.py":
        raise SystemExit("Please execute script from its directory")
    
    demo()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.check import check

check()


import src.utils.logger as log
import src.utils.path as pth
import src.parser.toml as tml
from src.utils.tools import download, extract

from src.run import run

from shutil import rmtree


def demo():
    log.init()
    
    # Downloading data from URLs and extracting downloaded files

    base_url = tml.value('demo', 'datasets', 'url')

    size = tml.value('demo', 'datasets', 'size')
    if size not in ['tiny', 'small', 'medium', 'big']:
        log.error(''.join(['\"', size, '\": unrecognized demo size, set to \"tiny\" by default']))
        size = 'tiny'

    note_url = ''.join([base_url, 'note_dataset_', size, '.tar.gz'])
    fx_url = ''.join([base_url, 'ir_dataset_', size, '.zip'])

    dry_dpath = tml.value('demo', 'dnames', 'input_dry')
    fx_dpath = tml.value('demo', 'dnames', 'input_fx')

    log.info("Downloading and extracting dataset(s)")
    
    if not pth.__exists(dry_dpath) and not pth.__exists(fx_dpath):  
        note_fname, fx_fname = download(note_url), download(fx_url)
        
        extract(note_fname, dry_dpath)
        extract(fx_fname, fx_dpath)
    elif not pth.__exists(dry_dpath) and pth.__exists(fx_dpath):
        note_fname = download(note_url)
        
        extract(note_fname, dry_dpath)
    elif pth.__exists(dry_dpath) and not pth.__exists(fx_dpath):
        fx_fname = download(fx_url)
        
        extract(fx_fname, fx_dpath)
    else:
        log.info("Skipping downloading since notes and IRs are still here, remove them if you changed demo mode")

    # Executing main script
    
    wet_dpath = tml.value('demo', 'dnames', 'output')

    if pth.__exists(wet_dpath):
        log.debug("Removing lastly generated samples")
        rmtree(wet_dpath)

    run(dry_dpath, fx_dpath, wet_dpath)

    log.shutdown()


if __name__ == '__main__':
    if __file__.replace('./', '') != "demo.py":
        raise SystemExit("Please execute script from its directory")
    
    demo()

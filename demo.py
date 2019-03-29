#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import src.utils.path as pth
import src.utils.logger as log
import src.parser.toml as tml
from src.run import run

import requests as req
from shutil import unpack_archive

    
def demo():
    log.init()
    
    # Scraping data from URLs
    
    base_url = tml.value('demo', 'datasets_url')

    note_url = ''.join([base_url, 'note_dataset_', tml.value('demo', 'size'), '.tar.gz'])
    fx_url = ''.join([base_url, 'ir_dataset_', tml.value('demo', 'size'), '.zip'])

    log.info('Scraping datasets of notes and impulse responses')

    note_fname, fx_fname = map(pth.__file_name, (note_url, fx_url))

    note_content, fx_content = req.get(note_url).content, req.get(fx_url).content

    pth.__write_file(note_fname, note_content)
    pth.__write_file(fx_fname, fx_content)

    # Extracting data

    dnames = tml.value('demo', 'dnames')

    unpack_archive(note_fname, dnames[0])
    unpack_archive(fx_fname, dnames[1])
    
    pth.__remove_file(note_fname)
    pth.__remove_file(fx_fname)

    # Execute main script

    run(*dnames)

    log.shutdown()


if __name__ == '__main__':
    if __file__.replace('./', '') != "demo.py":
        raise SystemExit("Please execute script from its directory")
    
    demo()

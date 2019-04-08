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

    dry_url = tml.value('demo', 'urls', 'dry')
    fx_url = tml.value('demo', 'urls', 'fx')

    dry_dpath = tml.value('demo', 'dnames', 'input_dry')
    fx_dpath = tml.value('demo', 'dnames', 'input_fx')

    log.info("Downloading and extracting dataset(s)")
    
    if not pth.__exists(dry_dpath) and not pth.__exists(fx_dpath):  
        dry_fname, fx_fname = download(dry_url), download(fx_url)
        
        extract(dry_fname, dry_dpath)
        extract(fx_fname, fx_dpath)
    elif not pth.__exists(dry_dpath) and pth.__exists(fx_dpath):
        dry_fname = download(dry_url)
        
        extract(dry_fname, dry_dpath)
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

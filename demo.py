#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Demo script that takes care of everything for you."""

from src.utils.decorators import mainify


@mainify
def demo():    
    import src.utils.logger as log
    import src.utils.path as pth
    import src.parser.toml as tml
    from src.utils.tools import download, extract
    
    
    # Downloading data from URLs and extracting downloaded files

    dry_url = tml.value('urls', section='demo', subkey='dry')
    fx_url = tml.value('urls', section='demo', subkey='fx')

    dry_dpath = tml.value('dnames', section='demo', subkey='input_dry')
    fx_dpath = tml.value('dnames', section='demo', subkey='input_fx')

    log.info("Downloading and extracting dataset(s)")
    
    if not pth.__exists(dry_dpath) and not pth.__exists(fx_dpath):  
        dry_fpath, fx_fpath = download(dry_url), download(fx_url)
        
        extract(dry_fpath, dry_dpath)
        extract(fx_fpath, fx_dpath)
    elif not pth.__exists(dry_dpath) and pth.__exists(fx_dpath):
        dry_fpath = download(dry_url)
        
        extract(dry_fpath, dry_dpath)
    elif pth.__exists(dry_dpath) and not pth.__exists(fx_dpath):
        fx_fpath = download(fx_url)
        
        extract(fx_fpath, fx_dpath)
    else:
        log.warning("\"{0}\" and \"{1}\" already exist, skipping downloading".format(dry_dpath, fx_dpath))

    return dry_dpath, fx_dpath, tml.value('dnames', section='demo', subkey='output')


if __name__ == '__main__':
    demo()

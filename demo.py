#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def demo():    
    import src.utils.logger as log
    import src.utils.path as pth
    import src.parser.toml as tml
    from src.utils.tools import download, extract

    from src.run import run


    if __file__.replace('./', '') != "demo.py":
        raise SystemExit("Please execute script from its directory")
    
    log.init()
    
    # Downloading data from URLs and extracting downloaded files

    dry_url = tml.value('demo', 'urls', 'dry')
    fx_url = tml.value('demo', 'urls', 'fx')

    dry_dpath = tml.value('demo', 'dnames', 'input_dry')
    fx_dpath = tml.value('demo', 'dnames', 'input_fx')

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

    # Executing main script

    run(dry_dpath, fx_dpath, tml.value('demo', 'dnames', 'output'))

    log.shutdown()


if __name__ == '__main__':
    from src.utils.check import check

    check()
    demo()

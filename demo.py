#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Demo script that takes care of everything for you."""

from src.utils.decorators import logify
from src.run import run


@logify
def demo():    
    import src.utils.logger as log
    import src.utils.path as pth
    import src.parser.toml as tml
    from src.utils.tools import download, extract
    
    
    # Downloading data from URLs and extracting downloaded files

    dry_url = tml.value('urls', section='demo', subkey='dry')
    fx_url = tml.value('urls', section='demo', subkey='fx')

    dry_dpath = tml.value('dnames', section='demo', subkey='input')
    fx_fname = tml.value('fx_name', section='demo')

    log.info("Downloading and extracting dataset and fx")

    fx_fpath = download(fx_url)
    pth.__rename_file(fx_fpath, fx_fname)
    
    if not pth.__exists(dry_dpath):
        dry_fpath = download(dry_url)
        extract(dry_fpath, dry_dpath)
    else:
        log.warning("\"{0}\" already exist, skipping dataset downloading".format(dry_dpath))

    run(dry_dpath, fx_fname, tml.value('dnames', section='demo', subkey='output'))


if __name__ == '__main__':
    demo()

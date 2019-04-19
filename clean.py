#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Remove files and directories created from running main script or demo script.

Apart from directory containing saved models.
"""

from src.utils.decorators import logify


@logify
def clean():
    import src.utils.path as pth
    import src.utils.logger as log
    import src.parser.toml as tml

    from shutil import rmtree

    log.info("Cleaning project")

    pth.__remove_file(tml.value('json', section='data', subkey='fname'))
    pth.__remove_file(tml.value('numpy', section='data', subkey='fname'))
    
    dnames = tml.value('dnames', section='demo')
    if pth.__exists(dnames['input']):
        rmtree(dnames['input'])
    if pth.__exists(dnames['output']):
        rmtree(dnames['output'])
    pth.__remove_file(tml.value('fx_name', section='demo'))

    dnames = tml.value('dnames', section='neuralnet')
    if pth.__exists(dnames['predictions']):
        rmtree(dnames['predictions'])

    
if __name__ == '__main__':
    clean()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.check import check

check()


from src.utils.tools import usage
import src.utils.logger as log

from src.run import run

import sys


def main():
    log.init()

    run(*sys.argv[1:])

    log.shutdown()


if __name__ == '__main__':
    if len(sys.argv) < 4:
        raise SystemExit(usage(__file__.replace('./', ''), ['path/to/dry/signals/dir', 'path/to/impulse/responses/dir', 'path/to/output/dir']))
    
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main script used as a wrapper around 'run.py' located in src."""


def main():
    import sys

    if len(sys.argv) < 3:
        raise SystemExit(usage(__file__.replace('./', ''), required_args=['path/to/dry/signals/dir', 'path/to/impulse/responses/dir'], optional_args=['path/to/output/dir']))
    
    from src.utils.tools import usage
    import src.utils.logger as log

    from src.run import run

    
    log.init()

    run(*sys.argv[1:])

    log.shutdown()


if __name__ == '__main__':
    from src.utils.check import check

    check()
    main()

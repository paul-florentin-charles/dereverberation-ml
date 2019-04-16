#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main script to run project."""

from src.utils.decorators import mainify


@mainify
def main():
    from src.utils.tools import usage

    import sys
    

    if len(sys.argv) < 3:
        raise SystemExit(usage(__file__.replace('./', ''), required_args=['path/to/dry/signals/dir', 'path/to/impulse/responses/dir'], optional_args=['path/to/output/dir']))

    return sys.argv[1:]


if __name__ == '__main__':
    main()

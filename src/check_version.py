# -*- coding: utf-8 -*-

# TODO: wrap pathlib objects with str(), because these are only supported in python 3.7 and not in 3.5 for instance

import sys, six


def check_version():
    print(''.join(['Running project with Python ', str(sys.version_info.major), '.', str(sys.version_info.minor), '.', str(sys.version_info.micro)]))
    if not six.PY3:
        raise SystemExit("Python 3 is required. Please update your version or run with the appropriate program")

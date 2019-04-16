# -*- coding: utf-8 -*-

"""Wrapper for built-in 'logging' module of python."""

import logging as lgn
import src.utils.colors as clrs
import src.parser.toml as tml


def init():
    """Init logger and colors."""
    clrs.start()
    _level = tml.value('level', section='logger')
    if _level.upper() not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        print(clrs.red("[CRITICAL] \"{0}\": {1}".format(_level, "unrecognized logging level")))
        clrs.close()
        raise SystemExit
            
    lgn.basicConfig(format='{%(asctime)s} %(message)s', level=_level.upper(), datefmt='%I:%M:%S')

def shutdown():
    """Shutdown logger and colors."""
    lgn.shutdown()
    clrs.close()
    
def debug(msg):
    """Display debug message."""
    lgn.debug(clrs.dim("[DEBUG] {0}".format(msg)))

def info(msg):
    """Display info message."""
    lgn.info(clrs.bright("[INFO] {0}".format(msg)))
 
def warning(msg):
    """Display warning message."""
    lgn.warning(clrs.yellow("[WARNING] {0}".format(msg)))

def error(msg):
    """Display error message."""
    lgn.error(clrs.magenta("[ERROR] {0}".format(msg)))

def critical(msg):
    """Display critical message and exit program."""
    lgn.critical(clrs.red("[CRITICAL] {0}".format(msg)))
    shutdown()
    raise SystemExit

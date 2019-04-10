# -*- coding: utf-8 -*-

import logging as lgn
import src.utils.colors as clrs
import src.parser.toml as tml


def init():
    """Inits logger and colors"""
    clrs.start()
    _level = tml.value('logger', 'level')
    if _level.upper() not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        print(clrs.red("[CRITICAL] \"{0}\": {1}".format(_level, "unrecognized logging level")))
        clrs.close()
        raise SystemExit
            
    lgn.basicConfig(format='{%(asctime)s} %(message)s', level=_level.upper(), datefmt='%I:%M:%S')

def shutdown():
    """Shutdowns logger and colors"""
    lgn.shutdown()
    clrs.close()
    
def debug(msg):
    lgn.debug(clrs.dim("[DEBUG] {0}".format(msg)))

def info(msg):
    lgn.info(clrs.bright("[INFO] {0}".format(msg)))
 
def warning(msg):
    lgn.warning(clrs.yellow("[WARNING] {0}".format(msg)))

def error(msg):
    lgn.error(clrs.magenta("[ERROR] {0}".format(msg)))

def critical(msg):
    lgn.critical(clrs.red("[CRITICAL] {0}".format(msg)))
    shutdown()
    raise SystemExit

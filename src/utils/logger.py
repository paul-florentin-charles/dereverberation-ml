# -*- coding: utf-8 -*-

import logging as lgn
import src.utils.colors as clrs
import src.parser.toml as tml


def init():
    """Inits logger and colors"""
    clrs.start()
    _level = tml.value('logger', 'level')
    if _level.upper() not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        print(clrs._red_("[CRITICAL] \"{0}\": {1}".format(_level, "unrecognized logging level")))
        clrs.close()
        raise SystemExit
            
    lgn.basicConfig(format='{%(asctime)s} %(message)s', level=_level.upper(), datefmt='%I:%M:%S')

def shutdown():
    """Shutdowns logger and colors"""
    lgn.shutdown()
    clrs.close()
    
def debug(msg):
    lgn.debug(clrs._dim_("[DEBUG] {0}".format(msg)))

def info(msg):
    lgn.info(clrs._bright_("[INFO] {0}".format(msg)))
 
def warning(msg):
    lgn.warning(clrs._yellow_("[WARNING] {0}".format(msg)))

def error(msg):
    lgn.error(clrs._magenta_("[ERROR] {0}".format(msg)))

def critical(msg):
    lgn.critical(clrs._red_("[CRITICAL] {0}".format(msg)))
    shutdown()
    raise SystemExit

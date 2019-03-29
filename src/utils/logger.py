# -*- coding: utf-8 -*-

import logging as lgn
import src.utils.colors as clrs
import src.parser.toml as tml


def init():
    clrs.start()
    _level = tml.value('logger', 'level')
    if _level.upper() not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        lgn.basicConfig(format='{%(asctime)s} %(message)s', datefmt='%I:%M:%S')
        critical(''.join(['\"', _level, '\": unrecognized logging level']))
            
    lgn.basicConfig(format='{%(asctime)s} %(message)s', level=_level.upper(), datefmt='%I:%M:%S')

def shutdown():
    lgn.shutdown()
    clrs.close()
    
def debug(msg):
    lgn.debug(clrs._dim_(''.join(["[DEBUG] ", msg])))

def info(msg):
    lgn.info(clrs._bright_(''.join(["[INFO] ", msg])))
 
def warning(msg):
    lgn.warning(clrs._yellow_(''.join(["[WARNING] ", msg])))

def error(msg):
    lgn.error(clrs._magenta_(''.join(["[ERROR] ", msg])))

def critical(msg):
    lgn.critical(clrs._red_(''.join(["[CRITICAL] ", msg])))
    shutdown()
    raise SystemExit

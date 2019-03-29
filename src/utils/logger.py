# -*- coding: utf-8 -*-

import logging as lgn
import src.utils.colors as clrs


def init(_level=lgn.DEBUG):
    lgn.basicConfig(format='{%(asctime)s} %(message)s',
                    level=_level,
                    datefmt='%I:%M:%S')

def shutdown():
    lgn.shutdown()
    
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

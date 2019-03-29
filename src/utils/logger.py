# -*- coding: utf-8 -*-

import logging as lgn
import src.utils.colors as clrs
import src.parser.toml as tml


def init():
    clrs.start()
    lgn.basicConfig(format='{%(asctime)s} %(message)s', level=tml.value('logger', 'level').upper(), datefmt='%I:%M:%S')

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
    raise SystemExit(lgn.critical(clrs._red_(''.join(["[CRITICAL] ", msg]))))

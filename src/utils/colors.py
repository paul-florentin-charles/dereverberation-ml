# -*- coding: utf-8 -*-

"""
Module to enhance your strings with colors and emphase
"""

from colorama import Fore, Style, init, deinit


def start():
    init()

def close():
    deinit()

def __fore__(msg, color):
    return ''.join([eval('Fore.{0}'.format(color.upper())), msg, Fore.RESET])

def __style__(msg, style):
    return ''.join([eval('Style.{0}'.format(style.upper())), msg, Style.RESET_ALL])

def _blue_(msg):
    '''Returns colorized <msg> in blue'''
    return __fore__(msg, 'blue')

def _cyan_(msg):
    '''Returns colorized <msg> in cyan'''
    return __fore__(msg, 'cyan')

def _green_(msg):
    '''Returns colorized <msg> in green'''
    return __fore__(msg, 'green')

def _black_(msg):
    '''Returns colorized <msg> in black'''
    return __fore__(msg, 'black')

def _red_(msg):
    '''Returns colorized <msg> in red'''
    return __fore__(msg, 'red')

def _yellow_(msg):
    '''Returns colorized <msg> in yellow'''
    return __fore__(msg, 'yellow')

def _magenta_(msg):
    '''Returns colorized <msg> in magenta'''
    return __fore__(msg, 'magenta')

def _bright_(msg):
    '''Returns brightened <msg>, typically similar to bold font'''
    return __style__(msg, 'bright')

def _dim_(msg):
    '''Returns <msg> with a sober grey-like font'''
    return __style__(msg, 'dim')


"""
def _blue_(msg):
    '''Returns colorized <msg> in blue'''
    return ''.join([Fore.BLUE, str(msg), Fore.RESET])

def _cyan_(msg):
    '''Returns colorized <msg> in cyan'''
    return ''.join([Fore.CYAN, str(msg), Fore.RESET])

def _green_(msg):
    '''Returns colorized <msg> in green'''
    return ''.join([Fore.GREEN, str(msg), Fore.RESET])

def _black_(msg):
    '''Returns colorized <msg> in black'''
    return ''.join([Fore.BLACK, str(msg), Fore.RESET])

def _red_(msg):
    '''Returns colorized <msg> in red'''
    return ''.join([Fore.RED, str(msg), Fore.RESET])

def _yellow_(msg):
    '''Returns colorized <msg> in yellow'''
    return ''.join([Fore.YELLOW, str(msg), Fore.RESET])

def _magenta_(msg):
    '''Returns colorized <msg> in magenta'''
    return ''.join([Fore.MAGENTA, str(msg), Fore.RESET])

def _bright_(msg):
    '''Returns brightened <msg>, typically similar to bold font'''
    return ''.join([Style.BRIGHT, str(msg), Style.RESET_ALL])

def _dim_(msg):
    '''Returns <msg> with a sober grey-like font'''
    return ''.join([Style.DIM, str(msg), Style.RESET_ALL])
"""

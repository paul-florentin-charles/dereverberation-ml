# -*- coding: utf-8 -*-

"""Module to enhance your strings with colors and emphase."""

from colorama import Fore, Style, init, deinit


# Init and end 

def start():
    """Initializes 'colorama' module"""
    init()

def close():
    """Terminates 'colorama' module"""
    deinit()

# Colors and styles
    
def blue(msg):
    """Returns colorized <msg> in blue"""
    return __fore(msg, 'blue')

def cyan(msg):
    """Returns colorized <msg> in cyan"""
    return __fore(msg, 'cyan')

def green(msg):
    """Returns colorized <msg> in green"""
    return __fore(msg, 'green')

def black(msg):
    """Returns colorized <msg> in black"""
    return __fore(msg, 'black')

def red(msg):
    """Returns colorized <msg> in red"""
    return __fore(msg, 'red')

def yellow(msg):
    """Returns colorized <msg> in yellow"""
    return __fore(msg, 'yellow')

def magenta(msg):
    """Returns colorized <msg> in magenta"""
    return __fore(msg, 'magenta')

def bright(msg):
    """Returns brightened <msg>, typically similar to bold font"""
    return __style(msg, 'bright')

def dim(msg):
    """Returns <msg> with a sober grey-like font"""
    return __style(msg, 'dim')

def __fore(msg, color):
    """Returns <msg> as printable string with color <color>"""
    return ''.join([eval('Fore.{0}'.format(color.upper())), msg, Fore.RESET])

def __style(msg, style):
    """Returns <msg> as printable string with style <style>"""
    return ''.join([eval('Style.{0}'.format(style.upper())), msg, Style.RESET_ALL])

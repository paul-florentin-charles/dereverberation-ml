# -*- coding: utf-8 -*-

"""Module to enhance your strings with colors and emphase."""

from colorama import Fore, Style, init, deinit


# Init and end 

def start():
    """Initialize 'colorama' module."""
    init()

def close():
    """Terminate 'colorama' module."""
    deinit()

# Colors and styles
    
def blue(msg):
    """Return colorized <msg> in blue"""
    return __fore(msg, 'blue')

def cyan(msg):
    """Return colorized <msg> in cyan"""
    return __fore(msg, 'cyan')

def green(msg):
    """Return colorized <msg> in green"""
    return __fore(msg, 'green')

def black(msg):
    """Return colorized <msg> in black"""
    return __fore(msg, 'black')

def red(msg):
    """Return colorized <msg> in red"""
    return __fore(msg, 'red')

def yellow(msg):
    """Return colorized <msg> in yellow"""
    return __fore(msg, 'yellow')

def magenta(msg):
    """Return colorized <msg> in magenta"""
    return __fore(msg, 'magenta')

def bright(msg):
    """Return brightened <msg>, typically similar to bold font"""
    return __style(msg, 'bright')

def dim(msg):
    """Return <msg> with a sober grey-like font"""
    return __style(msg, 'dim')

def __fore(msg, color):
    """Return <msg> as printable string with color <color>"""
    return ''.join([eval('Fore.{0}'.format(color.upper())), msg, Fore.RESET])

def __style(msg, style):
    """Return <msg> as printable string with style <style>"""
    return ''.join([eval('Style.{0}'.format(style.upper())), msg, Style.RESET_ALL])

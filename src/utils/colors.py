# -*- coding: utf-8 -*-

"""
Module to enhance your strings with colors and emphase
"""

from colorama import Fore, Style


def _blue_(string):
    '''Returns colorized <string> in blue'''
    return ''.join([Fore.BLUE, str(string), Fore.RESET])

def _cyan_(string):
    '''Returns colorized <string> in cyan'''
    return ''.join([Fore.CYAN, str(string), Fore.RESET])

def _green_(string):
    '''Returns colorized <string> in green'''
    return ''.join([Fore.GREEN, str(string), Fore.RESET])

def _black_(string):
    '''Returns colorized <string> in black'''
    return ''.join([Fore.BLACK, str(string), Fore.RESET])

def _red_(string):
    '''Returns colorized <string> in red'''
    return ''.join([Fore.RED, str(string), Fore.RESET])

def _yellow_(string):
    '''Returns colorized <string> in yellow'''
    return ''.join([Fore.YELLOW, str(string), Fore.RESET])

def _magenta_(string):
    '''Returns colorized <string> in magenta'''
    return ''.join([Fore.MAGENTA, str(string), Fore.RESET])

def _bright_(string):
    '''Returns brightened <string>, typically similar to bold font'''
    return ''.join([Style.BRIGHT, str(string), Style.RESET_ALL])

def _dim_(string):
    '''Returns <string> with a sober grey-like font'''
    return ''.join([Style.DIM, str(string), Style.RESET_ALL])

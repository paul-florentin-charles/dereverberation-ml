# -*- coding: utf-8 -*-

"""Set of decorators to give functions similar outputs."""


def stringify(func):
    """Decorator to convert function output to string or to a list of strings."""
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, list):
            return list(map(str, res))
        return str(res)
    
    return wrapper

def boolify(func):
    """Decorator to convert function output to boolean or to a list of booleans."""
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, list):
            return list(map(bool, res))
        return bool(res)
    
    return wrapper

def logify(func):
    """Decorator to convert function into loggable function.
    Act as a wrapper that does several things.
    """
    def wrapper(*args, **kwargs):
        from src.utils.check import check_all

        check_all()
        
        import src.utils.logger as log
        
        log.init()

        func(*args, **kwargs)
        
        log.shutdown()

    return wrapper

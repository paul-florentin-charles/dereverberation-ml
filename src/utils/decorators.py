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

def mainify(func):
    """Decorator to convert function into main function.
    Act as a wrapper that does several things.
    """
    def wrapper(*args, **kwargs):
        from src.utils.check import check
        
        check()

        import src.utils.logger as log
        import src.utils.path as pth
        import src.parser.toml as tml
        from src.run import run
        
        log.init()

        #TODO: Find a better way to check if file is executed from its directory  
        if pth.__file_name(pth.__working_dir()) != tml.value('repository_name'):
            log.critical("Please execute script from its directory")

        run(*func(*args, **kwargs))
        
        log.shutdown()

    return wrapper

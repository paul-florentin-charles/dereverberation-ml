# -*- coding: utf-8 -*- 

from __future__ import print_function

import sys


def check_all(verbose=False):
    """Check a bunch of stuff.
    To be called before running project.
    """
    check_version()
    #check_requirements(verbose)
    check_configuration(verbose)
    
def check_version():
    """Check if python version used to run project is Python 3."""
    print('Running project with Python', '.'.join(map(str, (sys.version_info.major, sys.version_info.minor, sys.version_info.micro))))
    
    if sys.version_info.major != 3:
        sys.exit("Python 3 is required, please update your version or run with the appropriate program")
        
def check_requirements(verbose=False):
    """Check if requirements listed in requirements files are installed."""
    import src.utils.path as pth
    from src.config import REQ_FNAME

    from importlib import import_module
    

    print("Checking requirements in {0}".format(REQ_FNAME))

    if not pth.__is_file(REQ_FNAME):
        raise SystemExit("Can't find \"{0}\" at the root".format(REQ_FNAME))

    ok = lambda msg: print("\"{0}\" [OK]".format(msg)) if verbose else None
    
    reqs = pth.__read_file(REQ_FNAME).split()
    reqs = [req[:req.find('=')] for req in reqs]

    for req in reqs:
        try:
            import_module(req)
            ok(req)
        except ImportError:
            raise SystemExit("\"{0}\" not found".format(req))
        
def check_configuration(verbose=False):
    """Check if values in configuration file are valid."""
    import src.parser.toml as tml
    import src.utils.path as pth
    from src.config import CFG_FNAME

    from itertools import repeat
    
    
    print("Checking values of {0}.".format(CFG_FNAME))

    if not pth.__is_file(CFG_FNAME):
        raise SystemExit("[CRITICAL] Can\'t find {0} at the root".format(CFG_FNAME))
    
    if verbose:
        ok = lambda msg: print("{0} [OK]".format(msg))
        notok = lambda msg: print("{0} [FAILED]".format(msg))
        section = lambda name: print("[{0}]".format(name.capitalize()))
    else:
        ok = notok = section = lambda _: None

    def check_value(vname, cond, msg):
        ok(vname) if cond else notok(vname) or sys.exit(msg)
        
    audio = 'audio'
        
    sr = tml.value('s_rate', section=audio)
    slen = tml.value('s_len', section=audio)
    bits = tml.value('bit_depth', section=audio)
    mod = tml.value('conv_mod', section=audio)
    fsiz = tml.value('f_size', section=audio)
    
    section(audio)
    
    check_value('sample rate', isinstance(sr, int) and sr > 0, "Sample rate must be a strictly positive integer")

    check_value('sample length', isinstance(slen, int) and slen > 0, "Sample length must be a strictly positive integer")

    check_value('bit depth', isinstance(bits, int) and bits > 0 and bits % 8 == 0, "Bit depth must be a strictly positive multiple of 8")

    check_value('convolution mode', isinstance(mod, str) and mod in ['full', 'same', 'valid'], "Convolution mode must be a string picked among \'full\', \'same\' and \'valid\'")

    check_value('frame size', isinstance(fsiz, int) and fsiz > 0, "Frame size must be a strictly positive integer")
    

    neuralnet = 'neuralnet'
        
    bsiz = tml.value('batch_size', section=neuralnet)
    epoc = tml.value('epochs', section=neuralnet)
    stps = tml.value('save_steps', section=neuralnet)
    lr = tml.value('learning_rate', section=neuralnet)
    dec = tml.value('decay', section=neuralnet)
    dirs = tml.value('dnames', section=neuralnet)
    dirs = [dirs[key] for key in dirs]

    section(neuralnet)

    check_value('batch size', isinstance(bsiz, int) and bsiz > 0, "Batch size must be a strictly positive integer")

    check_value('epochs', isinstance(epoc, int) and epoc > 0, "Epochs must be a strictly positive integer")

    check_value('save steps', isinstance(stps, int) and stps > 0, "Save steps must be a strictly positive integer")

    check_value('learning rate', isinstance(lr, (int, float)) and lr > 0, "Learning rate must be a strictly positive number")
    
    check_value('decay', isinstance(dec, (int, float)) and dec > 0, "Decay must be a strictly positive number")

    check_value('neuralnet directory names', all(map(isinstance, dirs, repeat(str))), "All neuralnet directory names must be strings")


    data = 'data'

    spls = tml.value('n_samples', section=data)
    json = tml.value('json', section=data, subkey='fname')
    stps = tml.value('json', section=data, subkey='save_steps')
    npz = tml.value('numpy', section=data, subkey='fname')
    
    section(data)

    check_value('number of samples', isinstance(spls, int) and spls > 0, "Number of samples must be a strictly positive integer")

    check_value('JSON file name', isinstance(json, str) and json.endswith('.json'), "JSON file name must be a string with \'.json\' suffix")

    check_value('save steps', isinstance(stps, int) and stps > 0, "Save steps must be a strictly positive integer")

    check_value('numpy file name', isinstance(npz, str) and npz.endswith('.npz'), "Numpy file name must be a string with \'.npz\' suffix")


    logger = 'logger'

    lvl = tml.value('level', section=logger)

    section(logger)

    check_value('debug level', isinstance(lvl, str) and lvl.lower() in ['debug', 'info', 'warning', 'error', 'critical'], "Debug level must be a string picked among \'debug\', \'info\', \'warning\', \'error\' and \'critical\'")


    demo = 'demo'

    fx = tml.value('fx_name', section=demo)
    urls = tml.value('urls', section=demo)
    urls = [urls[key] for key in urls]
    dirs = tml.value('dnames', section=demo)
    dirs = [dirs[key] for key in dirs]

    section(demo)

    check_value('fx file name', isinstance(fx, str), "FX file name must be a string")

    check_value('demo urls', all(map(isinstance, urls, repeat(str))), "Demo urls must be strings")

    check_value('demo directory names', all(map(isinstance, dirs, repeat(str))), "All demo directory names must be strings")

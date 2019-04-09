# -*- coding: utf-8 -*-

from __future__ import print_function

import sys


def check(verbose=False):
    check_version()
    check_config(verbose)
    
def check_version():
    print('Running project with Python', '.'.join([str(sys.version_info.major), str(sys.version_info.minor), str(sys.version_info.micro)]))
    
    if sys.version_info.major != 3:
        sys.exit("Python 3 is required, please update your version or run with the appropriate program.")
    
def check_config(verbose=False):
    import src.parser.toml as tml
    import src.utils.colors as clrs

    from itertools import repeat
    
    
    print(''.join(['Checking values of ', clrs._cyan_(tml.CFG_FNAME)]))
    
    if verbose:
        ok = lambda msg : print(msg + clrs._green_(" [OK]"))
        notok = lambda msg : print(msg + clrs._red_(" [FAILED]"))
        section = lambda name : print(clrs._bright_("[" + name  + "]"))
    else:
        ok = notok = section = lambda msg : None

    check_value = lambda vname, cond, msg : ok(vname) if cond else notok(vname) or sys.exit(msg)
    
    section("Audio")
    
    sr = tml.value('audio', 's_rate')
    slen = tml.value('audio', 's_len')
    bits = tml.value('audio', 'bit_depth')
    mod = tml.value('audio', 'conv_mod')
    fsiz = tml.value('audio', 'f_size')

    check_value('sample rate', isinstance(sr, int) and sr > 0, "Sample rate must be a strictly positive integer")

    check_value('sample length', isinstance(slen, int) and slen > 0, "Sample length must be a strictly positive integer")

    check_value('bit depth', isinstance(bits, int) and bits > 0 and bits % 8 == 0, "Bit depth must be a strictly positive multiple of 8")

    check_value('convolution mode', isinstance(mod, str) and mod in ['full', 'same', 'valid'], "Convolution mode must be a string picked among \'full\', \'same\' and \'valid\'")

    check_value('frame size', isinstance(fsiz, int) and fsiz > 0, "Frame size must be a strictly positive integer")

    section("Neural Network")

    fnam = tml.value('neuralnet', 'fname')
    bsiz = tml.value('neuralnet', 'batch_size')
    epoc = tml.value('neuralnet', 'epochs')
    lr = tml.value('neuralnet', 'learning_rate')
    dec = tml.value('neuralnet', 'decay')

    check_value('model file name', isinstance(fnam, str) and fnam.endswith('.h5'), "Model file name must be a string with \'.h5\' suffix") 

    check_value('batch size', isinstance(bsiz, int) and bsiz > 0, "Batch size must be a strictly positive integer")

    check_value('epochs', isinstance(epoc, int) and epoc > 0, "Epochs must be a strictly positive integer")

    check_value('learning rate', isinstance(lr, (int, float)) and lr > 0, "Learning rate must be a strictly positive number")
    
    check_value('decay', isinstance(dec, (int, float)) and dec > 0, "Decay must be a strictly positive number")
    
    section("Data")

    json = tml.value('data', 'json', 'fname')
    stps = tml.value('data', 'save_steps')
    npz = tml.value('data', 'numpy', 'fname')

    check_value('JSON file name', isinstance(json, str) and json.endswith('.json'), "JSON file name must be a string with \'.json\' suffix")

    check_value('save steps', isinstance(stps, int) and stps > 0, "Save steps must be a strictly positive integer")

    check_value('numpy file name', isinstance(npz, str) and npz.endswith('.npz'), "Numpy file name must be a string with \'.npz\' suffix")

    section("Logger")

    lvl = tml.value('logger', 'level')

    check_value('debug level', isinstance(lvl, str) and lvl.lower() in ['debug', 'info', 'warning', 'error', 'critical'], "Debug level mus be a string picked among \'debug\', \'info\', \'warning\', \'error\' and \'critical\'")

    section("Demo")

    url1 = tml.value('demo', 'urls', 'dry')
    url2 = tml.value('demo', 'urls', 'fx')
    ipt1 = tml.value('demo', 'dnames', 'input_dry')
    ipt2 = tml.value('demo', 'dnames', 'input_fx')
    out = tml.value('demo', 'dnames', 'output')

    check_value('demo urls', all(map(isinstance, (url1, url2), repeat(str))), "Demo urls must be strings")

    check_value('demo directory names', all(map(isinstance, (ipt1, ipt2, out), repeat(str))), "All demo directory names must be string")

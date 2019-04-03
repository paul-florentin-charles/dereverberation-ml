# -*- coding: utf-8 -*-

import sys, six


def check():
    check_version()
    check_config()

def check_version():
    print(''.join(['Running project with Python ', str(sys.version_info.major), '.', str(sys.version_info.minor), '.', str(sys.version_info.micro)]))
    if not six.PY3:
        raise SystemExit("Python 3 is required. Please update your version or run with the appropriate program")

def exi(msg):
    raise SystemExit("\n" + msg + "\n")
    
def check_config():
    import src.parser.toml as tml
    import src.utils.colors as clrs

    from itertools import repeat
    

    ok = lambda msg : print(msg + clrs._green_(" [OK]"))
    notok = lambda msg : print(msg + clrs._red_(" [FAILED]"))
    
    print(clrs._cyan_("Checking config"))
    
    print(clrs._bright_("Audio"))
    
    sr = tml.value('audio', 's_rate')
    slen = tml.value('audio', 's_len')
    bits = tml.value('audio', 'bit_depth')
    mod = tml.value('audio', 'conv_mod')
    
    if not isinstance(sr, int) or sr <= 0:
        notok("sample rate")
        exi("Sample rate must be a strictly positive integer")
    ok("sample rate")

    if not isinstance(slen, int) or slen <= 0:
        notok("sample length")
        exi("Sample length must be a strictly positive integer")
    ok("sample length")

    if not isinstance(bits, int) or bits <= 0 or bits % 8 != 0:
        notok("bit depth")
        exi("Bit depth must be a strictly positive mutiple of 8")
    ok("bit depth")

    if not isinstance(mod, str) or mod not in ['full', 'same', 'valid']:
        notok("convolution mode")
        exi("Convolution mode must be a string picked among \'full\', \'same\' and \'valid\'")
    ok("convolution mode")

    print(clrs._bright_("Neural Network"))

    fnam = tml.value('neuralnet', 'fname')
    bsiz = tml.value('neuralnet', 'batch_size')
    epoc = tml.value('neuralnet', 'epochs')
    lr = tml.value('neuralnet', 'learning_rate')

    if not isinstance(fnam, str) or not fnam.endswith('.h5'):
        notok("model file name")
        exi("Model file name must be a string with \'.h5\' suffix")
    ok("model file name")

    if not isinstance(bsiz, int) or bsiz <= 0:
        notok("batch size")
        exi("Batch size must be a strictly positive integer")
    ok("batch size")

    if not isinstance(epoc, int) or epoc <= 0:
        notok("epochs")
        exi("Epochs must be a strictly positive integer")
    ok("epochs")

    if not isinstance(lr, (int, float)) or lr <= 0:
        notok("learning rate")
        exi("Learning rate must be a strictly positive number")
    ok("learning rate")

    print(clrs._bright_("Data"))

    json = tml.value('data', 'json', 'fname')
    stps = tml.value('data', 'save_steps')
    npz = tml.value('data', 'numpy', 'fname')

    if not isinstance(json, str) or not json.endswith('.json'):
        notok("JSON file name")
        exi("JSON file name must be a string with \'.json\' suffix")
    ok("JSON file name")

    if not isinstance(stps, int) or stps <= 0:
        notok("save steps")
        exi("Save steps must be a strictly positive integer")
    ok("save steps")

    if not isinstance(npz, str) or not npz.endswith('.npz'):
        notok("numpy file name")
        exi("Numpy file name must be a string with \'.npz\' suffix")
    ok("numpy file name")

    print(clrs._bright_("Logger"))

    lvl = tml.value('logger', 'level')

    if not isinstance(lvl, str) or lvl.lower() not in ['debug', 'info', 'warning', 'error', 'critical']:
        notok("debug level")
        exi("Debug level mus be a string picked among \'debug\', \'info\', \'warning\', \'error\' and \'critical\'")
    ok("debug level")

    print(clrs._bright_("Demo"))

    size = tml.value('demo', 'datasets', 'size')
    url = tml.value('demo', 'datasets', 'url')
    ipt1 = tml.value('demo', 'dnames', 'input_dry')
    ipt2 = tml.value('demo', 'dnames', 'input_fx')
    out = tml.value('demo', 'dnames', 'output')

    if not isinstance(size, str) or size not in ['tiny', 'small', 'medium', 'big']:
        notok("demo size")
        exi("Demo size must be a string picked among \'tiny\', \'small\', \'medium\' and \'big\'")
    ok("demo size")

    if not isinstance(url, str):
        notok("demo url")
        exi("Demo url must be a string")
    ok("demo url")

    if not all(map(isinstance, (ipt1, ipt2, out), repeat(str))):
        notok("demo directory names")
        exi("All demo directory names must be string")
    ok("demo directory names")

# -*- coding: utf-8 -*-

import src.parser.toml as tml

from keras import optimizers as opt
from keras import losses as los
from keras import initializers as ini


# Numerical parameters

BATCH_SIZE = tml.value('neuralnet', 'batch_size')

EPOCHS = tml.value('neuralnet', 'epochs')

INPUT_SHAPE = (tml.value('audio', 's_len'), 1)

KERNEL_SIZE = 500

VALIDATION_SPLIT = 0.2


# Classes and functions

OPTIMIZER = opt.Adam(lr=tml.value('neuralnet', 'learning_rate'), decay=tml.value('neuralnet', 'decay'))

KERNEL_INITIALIZER = ini.TruncatedNormal()

BIAS_INITIALIZER = ini.Zeros()

LOSS = los.mean_squared_error


# Strings parameters

METRICS = ['accuracy']

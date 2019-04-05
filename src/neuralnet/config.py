# -*- coding: utf-8 -*-

import src.parser.toml as tml

from keras import optimizers as opt
from keras import losses as los
from keras import initializers as ini
from keras import activations as act


# Numerical parameters

BATCH_SIZE = tml.value('neuralnet', 'batch_size')

EPOCHS = tml.value('neuralnet', 'epochs')

INPUT_SHAPE = (tml.value('audio', 's_len'), 1)

KERNEL_SIZE = 500


# Classes and functions

OPTIMIZER = opt.Adam(lr=tml.value('neuralnet', 'learning_rate'), decay=tml.value('neuralnet', 'decay'))

KERNEL_INITIALIZER = ini.TruncatedNormal()

BIAS_INITIALIZER = ini.Zeros()

HIDDEN_ACTIVATION = act.linear

FINAL_ACTIVATION = act.tanh

LOSS = los.mean_squared_error


# Strings parameters

METRICS = ['accuracy']

CONVOLUTION_PADDING = 'same'

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

FRAME_SIZE = 1024

HOP_SIZE = 512


# Classes and functions

OPTIMIZER = opt.Adam(lr=tml.value('neuralnet', 'learning_rate'), decay=tml.value('neuralnet', 'decay'))

KERNEL_INITIALIZER = ini.TruncatedNormal()

BIAS_INITIALIZER = ini.Zeros()

HIDDEN_ACTIVATION = act.tanh

FINAL_ACTIVATION = act.linear

LOSS = los.mean_squared_error

METRICS = ['accuracy', LOSS]


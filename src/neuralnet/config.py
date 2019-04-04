# -*- coding: utf-8 -*-

import src.parser.toml as tml

from keras import optimizers as opt
from keras import losses as los
from keras import initializers as ini
from keras import metrics as met


# Numerical parameters

BATCH_SIZE = tml.value('neuralnet', 'batch_size')

EPOCHS = tml.value('neuralnet', 'epochs')

INPUT_SHAPE = (tml.value('audio', 's_len'), 1)

FRAME_SIZE = 2048

HOP_SIZE = 1024

# Classes and functions

OPTIMIZER = opt.Adam(lr=tml.value('neuralnet', 'learning_rate'))

KERNEL_INITIALIZER = ini.TruncatedNormal()

BIAS_INITIALIZER = ini.Zeros()

LOSS = los.mean_squared_error

METRICS = [met.categorical_accuracy, LOSS]


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


# Classes and functions

OPTIMIZER = opt.SGD(lr=tml.value('neuralnet', 'learning_rate'))

INITIALIZER = ini.TruncatedNormal()

LOSS = los.mean_squared_error

METRICS = [met.categorical_accuracy, LOSS]


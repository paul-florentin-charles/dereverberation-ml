# -*- coding: utf-8 -*-

import src.parser.toml as tml
import src.utils.path as pth

from keras import optimizers as opt
from keras import losses as los
from keras import initializers as ini
from keras import callbacks as cal


# Numerical parameters

BATCH_SIZE = tml.value('neuralnet', 'batch_size')

EPOCHS = tml.value('neuralnet', 'epochs')

INPUT_SHAPE = (tml.value('audio', 's_len'), 1)

KERNEL_SIZE = tml.value('audio', 'f_size')

VALIDATION_SPLIT = 0.2


# Classes and functions

OPTIMIZER = opt.Adam(lr=tml.value('neuralnet', 'learning_rate'), decay=tml.value('neuralnet', 'decay'))

LOSS = los.mean_squared_error

KERNEL_INITIALIZER = ini.TruncatedNormal()

BIAS_INITIALIZER = ini.VarianceScaling(mode='fan_avg', distribution='uniform')

CALLBACKS = [cal.ModelCheckpoint(pth.__join_path(tml.value('neuralnet', 'dnames', 'model'), 'model.{epoch:02d}-{val_loss:.3f}.h5'), period=tml.value('neuralnet', 'save_steps'))]


# Others

METRICS = ['accuracy']

# -*- coding: utf-8 -*-

import src.parser.toml as tml
import src.utils.path as pth

from keras import optimizers as opt
from keras import losses as los
from keras import initializers as ini
from keras import callbacks as cal


# Numerical parameters

BATCH_SIZE = tml.value('batch_size', section='neuralnet')

EPOCHS = tml.value('epochs', section='neuralnet')

INPUT_SHAPE = (tml.value('s_len', section='audio'), 1)

KERNEL_SIZE = tml.value('f_size', section='audio')

VALIDATION_SPLIT = 0.15


# Classes and functions

OPTIMIZER = opt.Adam(lr=tml.value('learning_rate', section='neuralnet'), decay=tml.value('decay', section='neuralnet'))

LOSS = los.mean_squared_error

KERNEL_INITIALIZER = ini.TruncatedNormal()

BIAS_INITIALIZER = ini.VarianceScaling(mode='fan_avg', distribution='uniform')

CALLBACKS = [cal.ModelCheckpoint(pth.__join_path(tml.value('dnames', section='neuralnet', subkey='model'), 'model.{epoch:02d}-{val_loss:.3f}.h5'), period=tml.value('save_steps', section='neuralnet'))]


# Others

METRICS = ['accuracy']

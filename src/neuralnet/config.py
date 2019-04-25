# -*- coding: utf-8 -*-

import src.parser.toml as tml
import src.utils.path as pth

from keras import optimizers as opt
from keras import losses as los
from keras import initializers as ini
from keras import callbacks as cal


# Numerical parameters

BATCH_SIZE = tml.value('model', section='neuralnet', subkey='batch_size')

EPOCHS = tml.value('model', section='neuralnet', subkey='epochs')

INPUT_SHAPE = (tml.value('s_len', section='audio'), 1)

KERNEL_SIZE = tml.value('f_size', section='audio')

N_LAYERS = tml.value('model', section='neuralnet', subkey='n_layers')

VALIDATION_SPLIT = tml.value('valid_split', section='neuralnet')

TEST_SPLIT = tml.value('tst_split', section='neuralnet')


# Classes and functions

OPTIMIZER = opt.Adam(lr=tml.value('model', section='neuralnet', subkey='learning_rate'), decay=tml.value('model', section='neuralnet', subkey='decay'))

LOSS = los.mean_squared_error

KERNEL_INITIALIZER = ini.TruncatedNormal()

BIAS_INITIALIZER = ini.VarianceScaling(mode='fan_avg', distribution='uniform')

CALLBACKS = [cal.ModelCheckpoint(pth.__join_path(tml.value('dnames', section='neuralnet', subkey='saved_models'), 'model.{epoch:02d}-{val_loss:.3f}.h5'), period=tml.value('save_steps', section='neuralnet'))]


# Others

METRICS = ['accuracy']

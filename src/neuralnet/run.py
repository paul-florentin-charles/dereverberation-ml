# -*- coding: utf-8 -*-

import src.utils.path as pth
import src.utils.logger as log
import src.parser.toml as tml
from src.datagen.io import _export
import src.neuralnet.utils as utls
from src.neuralnet.model import NeuralNetwork


def run_neuralnet(data, labels):
    """Run tool to train network on <data> and <labels>.
    Predict on <data> and export them as wave files.
    """
    # Shaping data and splitting them into train and test parts
    
    log.info("Shaping data")

    data, labels = map(utls.shape, (data, labels))
    train_data, test_data = utls.split_test(data, labels)

    # Building and training model

    mdl_dname = tml.value('dnames', section='neuralnet', subkey='model')
    if not pth.__is_empty(mdl_dname):
        log.warning("Model has already been trained in a previous session, picking up best model from \'{0}\' directory".format(mdl_dname))
        
        NN = NeuralNetwork(model=utls.load_best_model())
    else:
        log.info("Training model")
        
        pth.__make_dir(mdl_dname)
        NN = NeuralNetwork()
        NN.compile()
        NN.train(*train_data)

    # Making predictions using model

    log.info("Predicting with model")

    predictions = NN.predict(test_data[0])

    # Exporting predicted data along with expected data
    
    log.info("Exporting data")

    dnames = tml.value('dnames', section='neuralnet')
    
    _export(utls.unshape(predictions), dnames['predicted_labels'])
    _export(utls.unshape(test_data[1]), dnames['expected_labels'])

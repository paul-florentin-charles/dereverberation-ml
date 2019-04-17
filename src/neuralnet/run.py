# -*- coding: utf-8 -*-

import src.utils.path as pth
import src.parser.toml as tml
from src.datagen.io import _export
import src.neuralnet.utils as utls
from src.neuralnet.model import NeuralNetwork


def run_neuralnet(data, labels):
    """Run tool to train network on <data> and <labels>.
    Predict on <data> and export them as wave files.
    """
    log.info("Shaping data")

    data, labels = map(utls.shape, (data, labels))

    
    log.info("Training model")

    mdl_dname = tml.value('dnames', section='neuralnet', subkey='model')
    if not pth.__is_empty(mdl_dname):
        log.warning("Model has already been trained in a previous session, picking up best model from \'{0}\'".format(mdl_dname))
        NN = NeuralNetwork(model=utls.load_best_model())
    else:
        pth.__make_dir(mdl_dname)
        NN = NeuralNetwork()
        NN.compile()
        NN.train(data, labels)

        
    log.info("Predicting with model")

    _labels = NN.predict(data)

    
    log.info("Exporting data")

    pred_dname = tml.value('dnames', section='neuralnet', subkey='predictions')
    pth.__make_dir(pred_dname)
    _export(utls.unshape(_labels), pred_dname)

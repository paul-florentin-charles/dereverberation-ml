# -*- coding: utf-8 -*-

import src.utils.logger as log
import src.utils.path as pth
import src.parser.toml as tml
from src.datagen.io import generate_dataset, _export
from src.utils.data import write_data, read_data
from src.neuralnet.utils import shape, unshape
#from src.neuralnet.model import NeuralNetwork


def run(dry_dpath, fx_dpath, output_dir=None):
    # Dataset generation

    log.info("Generating dataset of wet samples")
        
    if output_dir is not None and pth.__exists(output_dir):
        log.warning("\"{0}\" already exists, skipping dataset generation".format(output_dir))
    else:
        generate_dataset(dry_dpath, fx_dpath, output_dir)
    
    # Shaping and storing data

    log.info("Retrieving data and saving it into a numpy file")

    npy_fname = tml.value('data', 'numpy', 'fname')
    if pth.__is_file(npy_fname):
        log.warning("\"{0}\" already exists, skipping data retrieval".format(npy_fname))
    else:
        write_data()

    # Reading data

    log.info("Reading data from numpy file and shaping it")

    data, labels = map(shape, read_data())

    """

    # Model training

    log.info("Training the model")

    NN = NeuralNetwork()
    NN.compile()
    pth.__make_dir(tml.value('neuralnet', 'dname'))
    NN.train(data, labels)

    # Model predicting

    log.info("Predicting using model")

    _labels = NN.predict(data)

    # Exporting data

    log.info("Exporting data")
    
    _export(unshape(_labels))

    """

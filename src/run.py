# -*- coding: utf-8 -*-

import src.utils.logger as log
import src.utils.path as pth
import src.parser.toml as tml
from src.datagen.io import generate_dataset, _export
from src.utils.data import write_data, read_data
#from src.neuralnet.utils import shape, unshape
#from src.neuralnet.model import NeuralNetwork


def run(dry_dpath, fx_dpath, output_dir=None):
    # Dataset generation

    log.info("Generating dataset of wet samples")

    if pth.__exists(output_dir):
        log.warning(''.join(["\"", output_dir, "\" already exists, skipping dataset generation"]))
    else:
        generate_dataset(dry_dpath, fx_dpath, output_dir)
    
    # Shaping and storing data

    log.info("Retrieving data and saving it into a numpy file")

    if pth.__is_file(tml.value('data', 'numpy', 'fname')):
        log.warning(''.join(["\"", tml.value('data', 'numpy', 'fname'), "\" already exists, skipping data retrieval"]))
    else:
        write_data()

    # Reading data

    log.info("Reading data from numpy file")

    data, labels = read_data()

    """
    # Model training

    log.info("Training the model")

    NN = NeuralNetwork()
    NN.compile()
    data, labels = map(shape, (data, labels))
    NN.train(data, labels)
    NN.save()

    # Model predicting

    log.info("Predicting")

    res = NN.predict(data[:20])
    _export(unshape(res))
    """

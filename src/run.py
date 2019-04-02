# -*- coding: utf-8 -*-

import src.utils.logger as log
from src.datagen.io import generate_dataset
from src.utils.data import retrieve_data, write_data
#from src.neuralnet.model import NeuralNetwork


def run(dry_dpath, fx_dpath, output_dir):
    # Dataset generation

    log.info('Generating dataset of wet samples')
    
    generate_dataset(dry_dpath, fx_dpath, output_dir)

    # Shaping and storing data

    log.info('Retrieving data and shaping it')

    data, labels = retrieve_data()

    log.info('Saving data in numpy files')

    write_data(data, labels)

    """
    # Model training

    log.info('Training the model')

    NN = NeuralNetwork()
    NN.compile()
    NN.train(data, labels)
    NN.save()
    """

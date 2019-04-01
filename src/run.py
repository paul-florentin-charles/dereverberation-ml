# -*- coding: utf-8 -*-

import src.utils.logger as log
from src.datagen.io import generate_dataset
from src.neuralnet.utils import retrieve_data, write_data, read_data
#import src.neuralnet.model as nnmodel


def run(dry_dpath, fx_dpath, output_dir):
    # Dataset generation

    log.info('Generating dataset of wet samples')
    
    generate_dataset(dry_dpath, fx_dpath, output_dir)

    # Model training

    log.info('Retrieving data and shaping it')

    data, labels = retrieve_data()

    log.info('Saving data in numpy files')

    write_data(data, labels)

    log.info('Training the model')

    """
    model = nnmodel._init()
    nnmodel._compile(model)
    nnmodel._train(model, data, labels)
    print(nnmodel._evaluate(model, data, labels))
    """

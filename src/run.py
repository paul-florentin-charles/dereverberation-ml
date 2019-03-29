# -*- coding: utf-8 -*-

import src.utils.logger as log
from src.datagen.io import generate_dataset
from src.neuralnet.utils import retrieve_data
#import src.neuralnet.model as nnmodel


def run(dry_dpath, fx_dpath, output_dir):
    # Dataset generation

    log.info('Generating dataset of wet samples')
    
    generate_dataset(dry_dpath, fx_dpath, output_dir)

    # Model training

    log.info('Shaping data to feed them to the model')

    data, labels = retrieve_data()

    log.info('Training the model')

    """
    model = nnmodel._init()
    nnmodel._compile(model)
    nnmodel._train(model, data, labels)
    print(nnmodel._evaluate(model, data, labels))
    """

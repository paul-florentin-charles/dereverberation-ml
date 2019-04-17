# -*- coding: utf-8 -*-

import src.utils.logger as log
import src.utils.path as pth
import src.parser.toml as tml
from src.datagen.io import generate_dataset
from src.utils.data import write_data, read_data


def run_datagen(dry_dpath, fx_dpath, output_dpath=None):
    """Run tool to generate dataset and write numpy data file.
    Return a couple (data, labels) to be used for training network.
    """
    log.info("Generating dataset of wet samples")
        
    if output_dpath is not None and pth.__is_dir(output_dpath):
        log.warning("\"{0}\" already exists, skipping dataset generation".format(output_dpath))
    else:
        generate_dataset(dry_dpath, fx_dpath, output_dpath)


    log.info("Retrieving data and saving it into a numpy file")

    npy_fname = tml.value('numpy', section='data', subkey='fname')
    if pth.__is_file(npy_fname):
        log.warning("\"{0}\" already exists, skipping data retrieval".format(npy_fname))
    else:
        write_data()


    log.info("Reading data from numpy file")

    data, labels = read_data()

    return data, labels

# -*- coding: utf-8 -*-

from src.datagen.run import run_datagen
#from src.neuralnet.run import run_neuralnet


def run(dry_dpath, fx_fpath, output_dpath=None):
    data, labels = run_datagen(dry_dpath, fx_fpath, output_dpath)
    #run_neuralnet(data, labels)

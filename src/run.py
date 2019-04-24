# -*- coding: utf-8 -*-

from src.datagen.run import run_datagen
#from src.neuralnet.run import run_neuralnet

#TODO: implement 2d-representation in a specific module
def run(dry_dpath, fx_fpath, output_dpath=None):
    data = run_datagen(dry_dpath, fx_fpath, output_dpath)
    #run_neuralnet(*data)

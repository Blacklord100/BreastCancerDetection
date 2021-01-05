#!/usr/bin/env python3
# test_with_pytest.py
#python -m pytest
import pytest
#from BreastCancerDetection.src import helpers,predict,preprocess,train_model
from BreastCancerDetection.src import helpers, predict
'''
def test_always_passes():
    assert True

def test_always_fails():
    assert False
'''
def test_preprocessing():
    config = helpers.load_config()
    data = helpers.load_data(**config['data_path_settings'])
    preprocess.preprocessing(data, **config['preprocessing_settings'])
'''
def test_load_model():
    config = helpers.load_config()
    clf = helpers.load_model("", **config['model_output'])

def test_train_model():
    config = helpers.load_config()
    train.model.train_model(**config)
'''
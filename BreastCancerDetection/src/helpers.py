import os
import yaml
import joblib
import datetime

import pandas as pd

def load_config(config_name="my_config.yaml", config_path="../config/"):
    with open(os.path.join(config_path, config_name),"r") as file:
        config = yaml.safe_load(file)
    return config

def load_data(data_directory,data_name):
    data = pd.read_csv(os.path.join(data_directory,data_name))
    return data

def append_timestamp(filename):
     timestamp = datetime.datetime.now().strftime("%Y-%H-%M")
     filename_with_timestamp = filename + "_" + str(timestamp) + ".pkl"
     return filename_with_timestamp

def dump_model(classifier, model_directory, model_name):
    joblib.dump(classifier, os.path.join(model_directory, append_timestamp(model_name)))

def load_model(model_timestamp, model_directory, model_name):
    if model_timestamp =="":
        return joblib.load(str(os.path.join(model_directory,model_name) + ".pkl"))
    else:
        return joblib.load(str(os.path.join(model_directory,model_name) + "_" + model_timestamp + ".pkl"))
    
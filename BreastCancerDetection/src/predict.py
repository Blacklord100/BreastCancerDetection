import os
import yaml
import joblib
import datetime
import argparse
import pandas as pd

import helpers


config = helpers.load_config()

clf = helpers.load_model("2021-22-34", **config['model_output'])


if __name__ == "__main__":
    # Parse command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", dest="config", nargs='?', const="my_config.yaml",
                        help="Absolute path to configuration file.")
    parser.add_argument("-tp", "--timestamp", dest="model_timestamp", nargs='?', const="",
                        help="Timestamp of the model, by default KNN_classifier.")
    
    parser.add_argument("-inp", "--input", dest="input", nargs='?', const="",
                    help="Input to predict.")

    args = parser.parse_args()

    # Ensure a config was passed to the script.
    if not args.config:
        print("No config file")
        exit()
    else:
        config = helpers.load_config(config_name=args.config)
        clf = helpers.load_model(args.model_timestamp, **config['model_output'])
        
    
else : 
    print('train_model imported')
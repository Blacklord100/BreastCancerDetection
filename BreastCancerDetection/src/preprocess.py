#python preprocessing.py -c my_config.yaml

# Import important packages
import pandas as pd
import numpy as np
import os
import yaml
import argparse

from BreastCancerDetection.src import helpers

#data = pd.read_csv(os.path.join("../data/", "breast-cancer-wisconsin.data"))

def preprocessing(data,replace, drop_columns):
    # replace "?" with -99999
    data = data.replace("?", replace['question_mark'])
    # drop id column
    data = data.drop(drop_columns, axis=1)
    return data

if __name__ == "__main__":
    # Parse command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", dest="config",
                        help="Absolute path to configuration file.")
    args = parser.parse_args()

    # Ensure a config was passed to the script.
    if not args.config:
        print("No configuration file provided.")
        exit()
    else:
        config = helpers.load_config(config_name=args.config)

    print(preprocessing(data, **config['preprocessing_settings']).head())

else : 
    print('preprocessing imported')
    

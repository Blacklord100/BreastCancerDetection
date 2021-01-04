import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib
import argparse

import helpers
from preprocess import preprocessing

config = helpers.load_config(config_name="my_config.yaml")

def train_model(data_path_settings, preprocessing_settings, data_split_settings, model_settings, model_output ):
    data = helpers.load_data(**data_path_settings)
    preprocessed_data = preprocessing(data, **preprocessing_settings)

    # Define X (independent variables) and y (target variable)
    X = np.array(preprocessed_data.drop(data_split_settings["target_name"], 1))
    y = np.array(preprocessed_data[data_split_settings["target_name"]])

    # split data into train and test set
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=data_split_settings["test_size"], random_state=42
    )

    # call our classifer and fit to our data
    clf = KNeighborsClassifier(**model_settings)
    # training the classifier
    clf.fit(X_train, y_train)

    # test our classifier
    result = clf.score(X_test, y_test)
    print("Accuracy score is. {:.1f}".format(result))

    # save our classifier in the model directory
    helpers.dump_model(clf, **model_output)


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
        train_model(**config)
    
else : 
    print('train_model imported')
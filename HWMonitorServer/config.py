# -*- coding: utf-8 -*-

import json
import os


def loadConfig():
    """
    Load configuration settings from a JSON file and return the configuration dictionary and the path to the file.

    Returns:
        tuple: A tuple containing the configuration dictionary and the absolute path to the configuration file.
    """
    # Construct the absolute path to the config file
    configFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

    # Set default config values
    bots, history, eye = [], True, False
    defaultConfig = {"Bots": bots, "History": history, "EYE": eye}

    # Load the contents of the config file into a dictionary
    try:
        with open(configFile) as inFile:
            config = json.load(inFile)
    except Exception as e:
        # If the file doesn't exist or is not valid JSON, create a new config file
        with open(configFile, "w") as outFile:
            config = defaultConfig
            json.dump(config, outFile, indent=4)

    # Check if "key" key is missing and add it if needed
    for key in defaultConfig:
        if key not in config:
            config[key] = eye

    # Write the updated config back to the file
    with open(configFile, "w") as outFile:
        json.dump(config, outFile, indent=4)

    return config, configFile


class Config:
    """
    A class for loading configuration settings.

    Attributes:
        config (dict): A dictionary containing configuration settings.
        configFile (str): The absolute path to the configuration file.
        botsName (list): A list of bot names.
        eyeFeature (bool): True or False
    """

    # Load the config file
    config, configFile = loadConfig()

    # Get the names of the bots
    botsName = config["Bots"]

    # Get the EYE setting
    eyeFeature = config["EYE"]

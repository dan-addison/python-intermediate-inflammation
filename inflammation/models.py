"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.

Functions:
    load_csv - load data from csv file
    daily_mean - calculate the mean inflammation value of all patients (rows) for each day
    daily_max - calculate the max inflammation value of all patients (rows) for each day
    daily_min - calculate the min inflammation value of all patients (rows) for each day

"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    :returns: numpy array containing the contents of the csv file
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: a 2D array of inflammation data. Each row represents a single patient. Columns represent days 0-40.
    :returns: An array of the mean inflammation measure across all patients per day
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: a 2D array of inflammation data. Each row represents a single patient. Columns represent days 0-40.
    :returns: An array of the max inflammation measure across all patients per day
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: a 2D array of inflammation data. Each row represents a single patient. Columns represent days 0-40.
    :returns: An array of the min inflammation measure across all patients per day
    """
    return np.min(data, axis=0)


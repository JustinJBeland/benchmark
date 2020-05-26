from scipy.io import loadmat
import numpy as np
import pandas as pd
from benchmark.core.datasets.regression import utils



def load_data(dataset_name):

    here = utils.__file__.replace('core/datasets/regression/utils.py','')

    # construct the filename
    filename = str(here + 'datasets/regression/' + dataset_name + '/' + dataset_name)

    if dataset_name == 'breastcancer':
        n, D, X, Y = load_mat(filename)
    elif dataset_name == 'gas':
        n, D, X, Y = load_mat(filename)
    elif dataset_name == 'residential':
        n, D, X, Y = load_xlsx_residential(filename)
    elif dataset_name == 'music68':
        n, D, X, Y = load_txt_music(filename)
    elif dataset_name == 'music116':
        n, D, X, Y = load_txt_music(filename)

    return n, D, X, Y


def load_mat(filename):

    # add extension 
    filename = filename + '.mat'

    # load the data anc convert to numpy array
    data = loadmat(filename)
    data = np.array(data['data'])

    # extract the number of samples and dimensionality of the input
    n = data.shape[0]
    D = data.shape[1] - 1

    # extract the inputs and targets
    X = data[:,0:D]
    Y = data[:,-1:]

    return n, D, X, Y

def load_txt_music(filename):

    # add extension 
    filename = filename + '.txt'

    # load the data anc convert to numpy array
    data = pd.read_csv(filename)
    data = data.values

    # remove header
    data = np.array(data).astype(np.float)

    # extract the inputs and out puts (longitude only)
    X = data[:, :-2]
    Y = np.reshape(data[:, -2:][:, 1],[-1,1])
    
    # find the number of samples and dimensionality
    n = X.shape[0]
    D = X.shape[1]

    return n, D, X, Y

def load_xlsx_residential(filename):

    # add extension 
    filename = filename + '.xlsx'

    # load the datafile
    data = pd.read_excel(filename)
    data = data.values

    # remove 
    # start year, start quarter, completion year and completion quarter (i.e., firts four rows)
    # and header
    data = np.array(data[1::, 4::]).astype(np.float)

    X = data[:, :-2]

    # take the first column of outputs only (could use both for a different purpose)
    Y = np.reshape(data[:, -2:][:, 0], [-1,1])

    # find the number of samples and dimensionality
    n = X.shape[0]
    D = X.shape[1]

    return n, D, X, Y


















from scipy.io import loadmat
import numpy as np


def load_data(dataset_name):

    # construct the filename
    filename = '../../../datasets/regression/' + dataset_name + '/' + dataset_name + '.mat'

    # load the data anc convert to numpy array
    data = loadmat('../../../datasets/regression/breastcancer/breastcancer.mat')
    data = np.array(data['data'])

    # extract the number of samples and dimensionality of the input
    n = data.shape[0]
    D = data.shape[1] - 1

    # extract the inputs and targets
    X = data[:,0:D]
    Y = data[:,-1:]

    return n, D, X, Y

dataset_name = 'breastcancer'
n, D, X, Y = load_data('breastcancer')
print(n, D)















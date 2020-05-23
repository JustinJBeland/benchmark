from scipy.io import loadmat
import numpy as np
from benchmark.core.datasets.regression import utils



def load_data(dataset_name):

    here = utils.__file__.replace('core/datasets/regression/utils.py','')

    # construct the filename
    filename = str(here + 'datasets/regression/' + dataset_name + '/' + dataset_name + '.mat')

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

'''
dataset_name = 'breastcancer'
n, D, X, Y = load_data('breastcancer')
print(n, D)
'''
















from benchmark.core.datasets.regression.utils import load_data

# load the data
n, D, X, Y = load_data('wine')

# print the stats
print('num samples    ', n)
print('dimensionality ', D)
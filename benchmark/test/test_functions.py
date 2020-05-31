from benchmark.test_functions.toy.toy_functions import get_function_definition
import torch
import matplotlib.pyplot as plt
import numpy as np
import math

# define problem
n = 10000
D = 10
objective = 'product_of_sines'

# get function info
fun, lb_x, ub_x = get_function_definition(objective, D)
lb_x = torch.Tensor(lb_x)
ub_x = torch.Tensor(ub_x)

# initialize points in X
X = torch.empty(n, D).uniform_(0,1)
X_scaled = torch.add(torch.mul(X, torch.sub(ub_x, lb_x)), lb_x)

# evaluate the objective
Y_scaled = torch.Tensor(fun(X_scaled.detach().numpy()))

print(X_scaled.shape)
print(Y_scaled.shape)


# plot the observations in 2-dimensions
if D == 2:
    plt.scatter(X_scaled[:,0], X_scaled[:,1], c=Y_scaled[:,0],marker='.',alpha=0.3)
    plt.colorbar()
    plt.show()


if objective == 'product_of_sines':
    x_test = np.reshape(-np.ones(D)*math.pi/2.0,[1,-1])
    print('minima is at ', fun(x_test))







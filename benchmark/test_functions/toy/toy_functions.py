import numpy as np

def rosenbrock(x):
    return np.sum(100.0*(x[:,1:]-x[:,:-1]**2.0)**2.0 + (1-x[:,:-1])**2.0,axis=1,keepdims=True)

def branin(x):
    x1 = x[:, 0]
    x2 = x[:, 1]
    y = np.square(x2 - (5.1/(4*np.square(np.pi)))*np.square(x1) + (5/np.pi)*x1 - 6) + 10*(1-(1./(8*np.pi)))*np.cos(x1) + 10
    return y.reshape(-1,1)

def quadratic(x):
    return np.sum(x**2.0, axis=1, keepdims=True)





def get_function_definition(objective, D):

    # specify a dictionary with function definitions and corresponding bounds
    opt_options = {'rosenbrock':{'fun':rosenbrock, 'lb':np.array([-1.5]*D), 'ub':np.array([3.0]*D)},
                   'branin':{'fun':branin, 'lb':np.array([-5.0] + [0.0]*(D-1)), 'ub':np.array([10.0] + [15.0]*(D-1))},
                   'quadratic':{'fun':quadratic,'lb':np.array([-1.0]*D), 'ub':np.array([1.0]*D)}}
    
    def_fun = opt_options[objective]['fun']
    lb = opt_options[objective]['lb']
    ub = opt_options[objective]['ub']

    return def_fun, lb, ub
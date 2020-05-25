
# Benchmark test functions and datasets

This repository contains a python wrapper for calling benchmark benchmark test functions and loading benchmark datasets to test machine learning algorithms

# Requirements
```
numpy==1.16.4
scipy==1.3.0
```

# Installation
```
python setup.py install
```
or
```
python setup.py develop
```

# Examples
```
python sfd/test/test_gp.py 
python sfd/test/test_decomp.py 
```

# Datasets:
* UCI breastcancer dataset (cancer)  (regression, single output) (n=194, D=33)
* UCI gas sensor dataset (gas)  (regression, single output) (n=2565, D=128)
* UCI residential building dataset (residential)  (regression, two outputs) (n=372, D=103)

# Test functions
* Rosenbrock (dim = n)



# Benchmark test functions and datasets

This repository contains a python wrapper for calling benchmark benchmark test functions and loading benchmark datasets to test machine learning algorithms

# Requirements
```
numpy==1.16.4
scipy==1.3.0
pytorch==1.5.0
```
* Note that pytorch is only used for testing the benchmark functions

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
python benchmark/test/test_gp.py 
```

# Datasets:
* UCI breastcancer dataset (cancer)  (regression, single output) (n=194, D=33)
* UCI gas sensor dataset (gas)  (regression, single output) (n=2565, D=128)
* UCI residential building dataset (residential)  (regression, two outputs) (n=372, D=103)
* UCI geographical original of music (music68)  (regression, two outputs) (n=1059, D=68)
* UCI geographical original of music (music116)  (regression, two outputs) (n=1059, D=116)
* UCI yacht dataset (yacht) (regression, single output) (n=308, D=6)
* UCI fertility dataset (fertility) (regression, single output) (n=100, D=9)
* UCI wine dataset (wine) (regression, single output) (n=1599, D=11)

# Test functions
* Rosenbrock (dim = D)
* Quadratic (dim = D)
* Branin (dim = D) ... Note dim usually is 2 but we can input any dimensionality we want and only the first two vars affect the response
* Rastrigin (dim = D)
* Product of Sines (dim = D)


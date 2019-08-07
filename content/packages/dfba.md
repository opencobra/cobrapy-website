+++
title = "dfba"
repo = "https://gitlab.com/davidtourigny/dynamic-fba"
date = "2019-08-07T13:03:00"
owner = "David S. Tourigny and Moritz E. Beber"
website = "https://pypi.org/project/dfba/"
tags = ["dynamic flux-balance analysis", "dfba"]
+++

The `dfba` project provides an object-oriented software package for dynamic
flux-balance analysis (DFBA) simulations using implementations of the direct
method or Algorithm 1 described in the paper [Harwood et al.,
2016](https://link.springer.com/article/10.1007/s00211-015-0760-3). The main
algorithms for solving embedded LP problems are written in `C++` and use the
[GLPK (GNU Linear Programming (LP) Kit)](https://www.gnu.org/software/glpk/)
and [SUNDIALS (Suite of Nonlinear and Differential/Algebraic Equation Solvers)
CVODE or IDA](https://computation.llnl.gov/projects/sundials). Extension modules
to [cobrapy](https://github.com/opencobra/cobrapy) are provided for easy
generation and simulation of DFBA models.


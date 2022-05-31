+++
title = "StrainDesign"
repo = "https://github.com/klamt-lab/straindesign"
date = "2022-05-31T12:00:00"
owner = "Philipp Schneider, Steffen Klamt"
website = "https://readthedocs.org/projects/straindesign"
tags = ["strain-design", "visualization", "cell-factories"]
+++

StrainDesign, a comprehensive Python package that integrates the most popular 
metabolic design algorithms, including nested strain optimization methods such 
as RobustKnock, OptCouple and OptKnock, as well as the more general minimal cut 
sets approach. The optimization approaches are embedded in individual modules, 
which can also be combined for setting up more elaborate strain design problems. 
Advanced features, such as the efficient integration of GPR-rules, the consideration 
of gene and reaction additions and of regulatory interventions are available for all
modules. The package uses state-of-the art preprocessing methods, supports CPLEX,
Gurobi, GLPK and SCIP and provides a number of enhanced tools for analyzing computed 
intervention strategies, for example, 2D and 3D plots of user-selected metabolic 
fluxes and yields. Furthermore, a user-friendlyGUI-based interface for the 
StrainDesign package has been implemented in the metabolic modeling software CNApy. 

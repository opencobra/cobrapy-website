+++
date = "2017-01-12T02:00:00-06:00"
+++

**cobrapy** is a python package that provides a simple interface to metabolic constraint-based reconstruction and analysis. 
```python
>>> import cobra
>>> import cobra.test
>>> model = cobra.test.create_test_model('textbook')
>>> model.metabolites[:3]
[<Metabolite 13dpg_c at 0x112b2d160>, 
 <Metabolite 2pg_c at 0x1024eb048>, 
 <Metabolite 3pg_c at 0x112b2d748>]
```

The package includes simple, object-oriented interfaces for model construction (including reading to/from sbml, matlab, and json formats) and implements commonly used COBRA methods such as flux balance analysis, flux variability analysis, and gene deletion analyses. 
```python
>>> model.optimize()
<Solution 0.87 at 0x11272c2b0>
>>> model.summary()
IN FLUXES        OUT FLUXES    OBJECTIVES
---------------  ------------  ----------------------
o2_e      21.8   h2o_e  29.2   Biomass_Ecol...  0.874
glc__D_e  10     co2_e  22.8
nh4_e      4.77  h_e    17.5
pi_e       3.21
```
**cobrapy** is a community-supported effort under active development.

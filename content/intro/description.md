+++
date = "2017-01-12T02:00:00-06:00"
+++

**cobrapy** is a python package that provides a simple interface to metabolic constraint-based reconstruction and analysis. 
```python
>>> import cobra
>>> model = cobra.io.read_sbml_model('Ec_core_flux1.xml')
>>> model.metabolites[:3]
[<Metabolite 13dpg_c at 0x112b2d160>, 
 <Metabolite 2pg_c at 0x1024eb048>, 
 <Metabolite 3pg_c at 0x112b2d748>]
```

The package includes simple, object-oriented interfaces for model construction (including reading to/from sbml, matlab, and json formats) and implements commonly used COBRA methods such as flux balance analysis, flux variability analysis, and gene deletion analyses. 
```python
>>> model.optimize()
<Solution 0.86 at 0x11272c2b0>
>>> model.summary()
IN FLUXES       OUT FLUXES    OBJECTIVES
--------------  ------------  ----------------------
o2_e     22.3   h2o_e  24.9   Biomass_Ecol...  0.861
glc_D_e  10     co2_e  23.3
pi_e      3.17  h_e     9.11
```
**cobrapy** is a community-supported effort under active development.

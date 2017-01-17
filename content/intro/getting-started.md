+++
date = "2017-01-12T02:00:00-06:00"
+++

Object-oriented COBRA models

```python
>>> import cobra
>>> import cobra.test
>>> model = cobra.test.create_test_model('textbook')
>>> model.metabolites[:3]
[<Metabolite 13dpg_c at 0x112b2d160>, 
 <Metabolite 2pg_c at 0x1024eb048>, 
 <Metabolite 3pg_c at 0x112b2d748>]
```

Flux balance analysis

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

Flux variability analysis

```python
>>> model.summary(fva=0.95)
IN FLUXES                       OUT FLUXES                      OBJECTIVES
------------------------------  ------------------------------  ----------------------
id          Flux  Range         id          Flux  Range         Biomass_Ecol...  0.874
--------  ------  ------------  --------  ------  ------------
o2_e       21.8   [19.9, 23.7]  h2o_e       29.2  [25, 30.7]
glc__D_e   10     [9.52, 10]    co2_e       22.8  [18.9, 24.7]
nh4_e       4.77  [4.53, 5.16]  h_e         17.5  [16.7, 22.4]
pi_e        3.21  [3.05, 3.21]  for_e        0    [0, 5.72]
                                ac_e         0    [0, 1.91]
                                acald_e      0    [0, 1.27]
                                pyr_e        0    [0, 1.27]
                                etoh_e       0    [0, 1.11]
                                lac__D_e     0    [0, 1.07]
                                succ_e       0    [0, 0.837]
                                akg_e        0    [0, 0.715]
                                glu__L_e     0    [0, 0.636]
```

Simple interfaces to COBRA methods
```python
>>> cobra.flux_analysis.optimize_minimal_flux(model)
<cobra.core.Solution.LegacySolution at 0x114551f60>
>>> model.metabolites.pep_c.summary(fva=.95)
PRODUCING REACTIONS -- Phosphoenolpyruvate (pep_c)
--------------------------------------------------
%       FLUX  RANGE           RXN ID      REACTION
----  ------  --------------  ----------  ----------------------------------------
100%  14.7    [9.96, 16.6]    ENO         2pg_c <=> h2o_c + pep_c
0%     0      [0, 8.58]       PPCK        atp_c + oaa_c --> adp_c + co2_c + pep_c
0%     0      [0, 8.58]       PPS         atp_c + h2o_c + pyr_c --> amp_c + 2.0...

CONSUMING REACTIONS -- Phosphoenolpyruvate (pep_c)
--------------------------------------------------
%       FLUX  RANGE           RXN ID      REACTION
----  ------  --------------  ----------  ----------------------------------------
68%   10      [9.52, 10]      GLCpts      glc__D_e + pep_c --> g6p_c + pyr_c
17%    2.5    [0, 11.7]       PPC         co2_c + h2o_c + pep_c --> h_c + oaa_c...
12%    1.76   [0, 12.3]       PYK         adp_c + h_c + pep_c --> atp_c + pyr_c
3%     0.454  [0.431, 0.454]  Biomass...  1.496 3pg_c + 3.7478 accoa_c + 59.81 ...
```


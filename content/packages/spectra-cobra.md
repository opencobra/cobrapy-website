+++
title = "spectra-cobra"
repo = "https://github.com/bisect-group/spectra-cobra"
date = "2026-10-04T12:00:00"
owner = "bisect-group"
website = "https://spectra-cobra.readthedocs.io"
tags = ["context-specific models", "model extraction", "flux consistency",
"metabolic reconstruction", "omics integration"]
+++

A Python port of the SPECTRA MATLAB package, built on cobrapy.

SPECTRA builds context-specific metabolic models: given a universal model and
a set of core reactions that a context is known to use, it returns the
smallest consistent network containing them. It provides

1. `spectra_cc`, a flux consistency check that reports and removes blocked
   reactions, under either a steady-state or an accumulation condition.
2. `spectra_me`, which extracts a context-specific model around a core set,
   with four network inference formulations: `minNetLP`, `minNetMILP`,
   `tradeOff` for signed omics evidence, and `growthOptim`.
3. `spectra_ccme`, which folds the consistency check into the extraction so
   that an inconsistent universal model can be used directly.
4. Alternative solutions, by core direction or pathway exclusion, for
   sampling the space of models consistent with the same evidence.

Implements: Kumar S, P., Sridhar, S., Alsmadi, N., Mahadevan, R., and Bhatt,
N. "Generalist method to reconstruct metabolic networks from multi-omics data
at large-scale." bioRxiv (2026).
DOI: https://doi.org/10.64898/2026.04.02.716249

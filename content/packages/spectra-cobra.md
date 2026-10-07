+++
title = "spectra-cobra"
repo = "https://github.com/bisect-group/spectra-cobra"
date = "2026-10-04T12:00:00"
owner = "bisect-group"
website = "https://spectra-cobra.readthedocs.io"
tags = ["metabolic reconstruction", "context-specific models", "gap-filling",
"community gap-filling", "minimal microbiome", "model extraction",
"flux consistency", "omics integration"]
+++

SPECTRA reconstructs metabolic networks from multi-omics data at a range of
biological scales: minimal reactomes, context-specific models, gap-filled
reconstructions, minimal microbiomes, microbial community models and
multi-tissue models. What changes between them is the universal model, the
evidence supplied and the objective chosen, not the routine called.

Two options give that range. `consistency_type` picks the steady state
`S v = 0` or the accumulation condition `S v >= 0` that gap filling needs.
`problem_type` picks the objective: minimise total flux, minimise reaction
count, maximise signed omics evidence, or maximise biomass against a flux
penalty.

`spectra_cc` removes blocked reactions, `spectra_me` extracts a network
around a set of core reactions, and `spectra_ccme` does both at once.
Alternative solutions come from core direction or pathway exclusion.

The accompanying paper reports a 56-fold speed-up over existing algorithms
for consistency-based reconstruction, with applications to 1,479 cancer cell
lines, 7,302 gap-filled AGORA2 reconstructions and synthetic gut microbiota.

Implements: Kumar S, P., Sridhar, S., Alsmadi, N., Mahadevan, R., and Bhatt,
N. "Generalist method to reconstruct metabolic networks from multi-omics data
at large-scale." bioRxiv (2026).
DOI: https://doi.org/10.64898/2026.04.02.716249

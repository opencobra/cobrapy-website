+++
title = "cameo"
repo = "https://github.com/biosustain/cameo"
name = "cameo"
date = "2017-01-13T11:00:01-06:00"
owner = "Biosustain"
website = "https://cameo.eu"
tags = ["Synthetic Biology", "strain design", "general modeling"]
+++

Cameo is a high-level python library developed to aid the strain design process in metabolic engineering projects. The library provides a modular framework of simulation methods, strain design methods, access to models, that targets developers that want custom analysis workflows.

Computationally heavy methods have been parallelized and can be run on a clusters using the IPython parallelization framework (see example and documentation for more details). The default fallback is python's multiprocessing library.

Furthermore, it exposes a high-level API to users that just want to compute promising strain designs.

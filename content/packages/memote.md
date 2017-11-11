+++
title = "memote"
repo = "https://github.com/opencobra/memote"
date = "2017-01-06T11:00:01-06:00"
owner = "opencobra"
website = "https://memote.readthedocs.io/"
tags = ["metabolic model", "metabolic reconstruction", "standardization",
"unit-testing", "cobra", "sbml"]
+++

Our goal in promoting this tool is to achieve two major shifts in the metabolic model building community:

1. Models should be version-controlled such that changes can be tracked and if necessary reverted. Ideally, they should be available through a public repository such as GitHub that will allow other researchers to inspect, share, and contribute to the model.
2. Models should, for the benefit of the community and for research gain, live up to certain standards and minimal functionality.

The memote tool therefore performs four subfunctions:

1. Create a skeleton git repository for the model.
2. Run the current model through a test suite that represents the community standard.
3. Generate an informative report which details the results of the test suite in a visually appealing manner.
4. (Re-)compute test statistics for an existing version controlled history of a metabolic model.

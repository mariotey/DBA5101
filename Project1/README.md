In Project 1, we aim to estimate the demand function of fish using data on fish sales in "Data-GP1-1.csv"

Firstly, we checked the appropriateness of our dataset and ensuring that all the data are in the right format. "data_cleaning.ipynb" shows our data cleaning process which ultimately allows us to produce "Data-GP1-1(updated).csv". This csv will be used for our subsequently analysis.

We then explore our data in "data_explore.ipynb" to visualize the distribution and portion of our dataset.

With a better understanding of the data, we formulated our structural and reduced form equation and decided that "Mon","Tue","Wed" and "Thu" should be our Exogenous variables. In "IV_test.ipynb", we attempt to find potential IVs that are suitable for our regression model and were able to narrow it down to 4 potential IV permutations.

In "model_select.ipynb", we evaluate the performance of our model with the 4 permutations of IVs.

Finally, in "base.ipynb", we decided to finalize on a model to estimate the demand function of fish.

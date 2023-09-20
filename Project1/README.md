In Project 1, we aim to estimate the demand function of fish using data on fish sales in **_"Data-GP1-1.csv"_**

Firstly, we checked for missing data and ensured that all of them are in the right format. **_"data_cleaning.ipynb"_** shows our data cleaning process which ultimately allows us to produce **_"Data-GP1-1(updated).csv"_**. This csv data will be used for our subsequent analysis.

We then explore our data in **_"data_explore.ipynb"_** to visualize the distribution and portion of our dataset.

With a better understanding of the data, we formulated our structural and reduced form equation and decided that _"Mon"_,_"Tue"_,_"Wed"_ and _"Thu"_ should be our Exogenous variables. In **_"IV_test.ipynb"_**, we attempt to find potential IVs that are suitable for our regression model and were able to narrow it down to 4 potential IV permutations.

In **_"model_select.ipynb"_**, we evaluate the performance of our model with the 4 permutations of IVs.

Finally, in **_"base.ipynb"_**, we decided to finalize on a model to estimate the demand function of fish.

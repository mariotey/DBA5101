In Project 1, we aim to estimate the demand function of fish using data on fish sales in **_"Data-GP1-1.csv"_**.

Firstly, we checked for missing data and ensured that all of them are in the right format. **_"data_cleaning.ipynb"_** details our data cleaning process which ultimately allows us to produce **_"Data-GP1-1(updated).csv"_**. This csv data will be used for our subsequent analysis.

We then explore our data by visualizing the distribution and proportion of our dataset in **_"data_explore.ipynb"_**.

With a better understanding of the data, we formulated our structural and reduced form equation and decided that _"Mon"_,_"Tue"_,_"Wed"_ and _"Thu"_ should be our Exogenous variables. In **_"IV_test.ipynb"_**, we attempt to find potential IVs that are suitable for our regression model and narrowed down to 4 iterations of potential IV.

In **_"model_select.ipynb"_**, we evaluate the performance of our model with the 4 iterations of IVs.

Finally, **_"base.ipynb"_** shows the finalized model that will be used to estimate the demand function of fish.

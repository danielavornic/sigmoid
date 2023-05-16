# Outlier Detection

During the last topic, you learned the art of plotting using matplotlib and seaborn in python. Also, we have learned what **Outliers** are and how to identify them. In this topic, you should explore a little bit more the given Data Set and plot the information about the outliers.

## Selected Data Set

Pokemon Classification Dataset. Available [here](https://bit.ly/3sJpeqn).

## Tasks

For this chapter, you will have to do the following:

- Import and prepare the Data Set.
- Find the 2 columns that correlate most significantly with the price column.
- Create a temporary subset using these 2 columns.
- Train and predict using the Isolation Forest, OneClassSVM, Elliptic Envelope, and LocalOutlierFactor.
- Create a grid 2x2 on scatter plots with the different colors for normal samples and outliers for each algorithm.
- Try to make a conclusion based on these plots.
- Find the number of outliers on the whole Data Set (without the target column) for different values of contamination for each outliers detection algorithm.
- Create for each algorithm the line plot showing the dependence of the number of outliers and the contamination value.
- Try to conclude.
- Split the Data Set into the train and test sets.
- Using the default settings of each outliers detection algorithm, find and remove the outliers from the Data Set, creating a subset.
- Train on the initial and the gotten subset of the following algorithms: LinearRegression and KNN Regressor.
- Find the accuracy of each combination of the prediction and outliers detection algorithms on the test subset.
- Create the table of the following structure.
- Make a conclusion based on the table that you got

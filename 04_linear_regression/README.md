# Linear Regression

In the majority of Machine Learning use-cases, following one or another form as a Data Scientist, you should create a model that predicts something. Be it a class, a numerical value, or a sequence of values. In this task, you will train your first Machine Learning Model - Linear Regression.

In this task, we invite you to train 2 models on the selected Data Set that should predict the target column. The models are the following:

- the LinearRegression from sklearn;
- the Lin_reg implementation offered in SMLH.

## Selected Data Set

Electric Motor Temperature. Available [here](https://bit.ly/3UuvaPV).

## Tasks

- Create a Jupyter notebook with a clean code.
- Study the correlation between features, find the features subset with the highest correlation with the target column, and try to explain from the business point of view why they have such a big correlation.
- Create a second set of data with the columns that have an absolute correlation between 0.5 and 0.8 with the target column.
- Split the data into 2 sub-sets using the train test split function from sklearn.
- Train a sklearn Linear Regression model on the data provided to you.
- Train a from-scratch implementation of Linear Regression on the train sub-set.
- Test the models on the test sets from the initial data set. For error metrics, use the model’s ’score’ function from the Linear Regression model.
- Split the data with the selected columns into 2 sub-sets using the train test split function from sklearn.
- Train a sklearn Linear Regression model on the data with selected columns (train subset).
- Train a from-scratch implementation of Linear Regression on the train sub-set.
- Test the models on the test sets from the initial data set. For error metrics, use the model’s ’score’ function from the sklearn Linear Regression model.
- Please try to interpret the results you are getting by comparing the error of the models you created.
- Please comment on your code.

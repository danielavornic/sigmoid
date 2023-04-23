# Missing Values

As you learned from the last topic, data rarely comes in a structured way with all values filled. Usually, the data comes with missing values along the way, which you need to handle, and this is what you will do in this homework.

## Selected Dataset

Chronic Kidney Disease Dataset. Available [here](https://bit.ly/3UejZKK).

## Tasks

For this chapter, you will have to do the following:

- Let’s begin by importing the Data Set.
- Create a (bar) plot showing the number of missing values in every column.
- Split the Data Set into the train and test sets.
- Create an instance of the SimpleImputer with the strategy set as **mean**.
- Create an instance of the SimpleImputer with the strategy set as **median**.
- Create an instance of the SimpleImputer with the strategy set as **most_frequent**.
- Create an instance of the SimpleImputer with the strategy set as **constant** and the **fill_value** = 0.
- Create an instance of the CDI from reparo.
- Create an instance of the FRNNI from reparo.
- Create an instance of the HotDeckImputation from reparo.
- Create an instance of the KNNImputer from reparo.
- Create an instance of the PMM from reparo.
- Create an instance of the SICE from reparo.
- Create an instance of the MICE from reparo.
- Train every imputer on the train Data Set.
- Fill in the missing values on the train and test subset.
- Train the following models on every set that you got after imputing the missing values:
  - Logistic Regression.
  - Gaussian Naive Bayes.
  - TreeDecisionClassifier.
  - RandomForest.
- Test each of the models on the test set and build the following table:

  | Imputation Algorithms | Prediction algorithms | Accuracy |
  | --------------------- | --------------------- | -------- |
  | ‎                     |                       |          |

- Conclude the results you got.

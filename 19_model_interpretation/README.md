# Model Interpretation

In the last topic, you learned how to interpret a model. In this homework, we invite you to apply all the knowledge to interpret the models' results on the Data Sets.

## Selected Data Sets

- Electric Motor Temperature Data Set. Available [here](https://bit.ly/3UuvaPV);

- Heart Failure Prediction Data Set. Available [here](https://bit.ly/3TR0yYU).

## Tasks

For this chapter, you will have to do the following:

- Import both Data Sets.
- Train a linear regression model on the regression Data Set and make a bar plot using the weights of the linear model. Interpret the plot.
- Generate the classification Data. Set the image showing the decision tree.
- For both Data sets, after it was cleaned, split them into the train and test subsets.
- On the train subsets of the regression Data Set to trail the following algorithms: Linear Regression and KNN Regression (bonus: try RandomForestRegression and DecissionTreeRegression).
- On the train subsets of the regression Data Set to trail the following algorithms: Logistic Regression, Gaussian Naive Bayes, and KNN Classifcator (bonus: try RandomForestClassification, DecissionTreeClassification, Bernoulli Naive Bayes, and Multinomial Naive Bayes).
- For each regression model, get the MSE, MAE, and RMSE on the test subset.
- For each classification model, get the Accuracy, Precision, Recall, and F1-Score.
- For each regression model, build the following table.

  | Estimator | MSE | MAE | RMSE |
  | --------- | --- | --- | ---- |
  | est 1     |     |     |      |
  | est 2     |     |     |      |
  | ...       |     |     |      |
  | est n     |     |     |      |

- For each classification model, build the following table.

  | Estimator | Accuracy | Precision | Recall | F1-Score |
  | --------- | -------- | --------- | ------ | -------- |
  | est 1     |          |           |        |          |
  | est 2     |          |           |        |          |
  | ...       |          |           |        |          |
  | est n     |          |           |        |          |

- Analyze the tables you got, make some conclusions, and choose the best regression and classification, models.
- Pick the best classification model and interpret it using shap: Create
  the following plots:
  - SHAP barplot.
  - SHAP waterfall plot.
  - SHAP beeswarm plot.
  - SHAP force plot.
- Make some conclusions on each plot.
- Pick the best regression model and interpret it using LIME. Find the samples with the highest difference between the target and predicted values. Interpret them with LIME and say what went wrong.
- Make some conclusions on each plot.

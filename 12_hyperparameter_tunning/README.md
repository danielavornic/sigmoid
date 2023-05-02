# Hyperparameter Tunning

In the last topic, you learned what **Hyperparameter Tuning** is. In this homework, we invite you to explore the effect of hyperparameters on the performance metrics of different models.

## Selected Datasets

Body Performance Data Set. Available [here](https://bit.ly/3FBtYWu);

Electric Motor Temperature Data Set. Available [here](https://bit.ly/3UuvaPV).

## Tasks

For this chapter, you will have to do the following:

- Import both Data Sets.
- Clean both Data Sets.
- Create a line plot with the number of neighbors of KNN on the X-axis and the model’s accuracy on the Y-axis on the classification Data Set.
- Create a line plot with the number of neighbors of KNN (Regression version) on the X-axis and the MSE of the model on the Y-axis on the regression Data Set.
- Create a heatmap using the TreeDecissionClassifier using the **max_depth** as X-axis, and **max_features** as the Y-axis and the color of the map should depend on the accuracy of the model on the classification Data Set for the **criterion = gini**.
- Create a heatmap using the TreeDecissionClassifier using the **max_depth** as X-axis, and **max_features** as Y-axis, and the color of the map should depend on the accuracy of the model on the classification Data Set for the **criterion = entropy**.
- Create a heatmap using the TreeDecissionRegression using the **max_depth** as X-axis, and **max_features** as Y-axis, and the color of the map should depend on the MSE of the model on the regression Data Set for the **criterion = friedman_mse**.
- Create a heatmap using the TreeDecissionRegression using the **max_depth** as X-axis, and **max_features** as Y-axis, and the color of the map should depend on the MSE of the model on the regression Data Set for the **criterion = poisson**.
- Create a line plot using the RandomForestClassifier containing 2 lines for **criterion = gini** and one for **criterion = entropy** on X-axis should be the **n_estimators** and one Y-axis the accuracy of the model on the classification Data Set.
- Create a line plot using the RandomForestRegressor containing 3 lines for **criterion = ”squared_error”**, **criterion = ”absolute_error”** and one for **criterion = ”poisson”**, on X-axis should be the **n_estimators** and one Y-axis the MSE of the model on the regression Data Set.
- Create a line plot using the SVC model containing 3 lines for **kernel= ’poly’, ’rbf ’, ’sigmoid’** on the X-axis should be the C and one Y-axis the accuracy of the model on the classification Data Set.
- Create a line plot using the SVR model containing 3 lines for **kernel= ’poly’, ’rbf ’, ’sigmoid’** on the X-axis should be the C and one Y-axis the MSE of the model on the regression Data Set.
- Please extract a conclusion for every plot that you make.

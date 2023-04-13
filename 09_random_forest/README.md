# Random Forest

Now that you learned how Decision Trees work, it’s time to move forward to the next level - **Random Forest**. In this homework, you will explore Random Forest, comparing it with the result from Decision Trees. You may use the same data set you used in the last homework.

## Selected Dataset

Pima Indians Diabetes Dataset. Available [here](https://bit.ly/3zqVZMs).

## Tasks

In this task, we invite you to train 2 models on the selected Data Set that should predict the class column. The models are the following:

- Let’s start with importing the Data Set.
- The next thing you are going to do is to create a visualization of the decision boundaries of the algorithm, to better understand how it works and compare it with the one of the Decision Tree.
- Choose the same 2 features from the last homework.
- Create the decision boundary graph of these features related to the target.
- Comment on the result that you got, and compare them with the one from Decision Trees homework.
  PS: More about decision boundary you can find [here](https://bit.ly/3U7ICc7).
- Random Forest, as Decision trees, has a lot of hyperparameters. Let’s explore how they influence the accuracy of the model. For every hyperparameter in this list, create a line plot where on the X-axis are hyperparameter values and on the Y-axis is the accuracy of the model
  for different hyperparameter settings:
  - _max_depth_
  - _min_samples_split_
  - _min_samples_leaf_
  - _min_weight_fraction_leaf_
  - _max_features_
  - _max_leaf_nodes_
  - _min_impurity_decrease_
    P.S. Always set random state the same.
- Comment on the impact of every hyperparameter on the model’s accuracy, especially comparing the Decision Trees results.
- Train a model with the best set of hyperparameters.

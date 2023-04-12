# Decision Trees

As you probably already learned, **Decision Trees** are very powerful and, at the same time, easy-to-understand Machine Learning algorithms. Doing this homework, you will train a couple of Decision tree algorithms and will try to dive deeper into how it works.

## Selected Dataset

Pima Indians Diabetes Dataset. Available [here](https://bit.ly/3zqVZMs).

## Tasks

In this task, we invite you to train 2 models on a selected Data Set that should predict the class column. The models are the following:

- Let’s, of course, start with importing the Data Set.
- The next thing you will do is create a visualization of the algorithm’s decision boundaries to understand better how it works.
- Choose 2 features of the Data Set with the highest absolute correlation with the target.
- Create the decision boundary graph of these features related to the target.
- Comment on the result that you got.

PS: More about decision boundary you can find [here](https://bit.ly/3U7ICc7).

- Decision trees have a lot of hyperparameters. Let’s explore how they influence the accuracy of the model. For every hyperparameter in this list, create a line plot where on the X-axis are hyperparameter values and on the Y-axis is the accuracy of the model for different hyperparameter settings:
  - _max depth_
  - _min samples split_
  - _min samples leaf_
  - _min weight f raction leaf_
  - _max f eatures_
  - _max leaf nodes_
  - _min impurity decrease_

P.S. Always set random state the same.

- Comment on the impact of every hyperparameter on the model’s accuracy.
- Train a model with the best set of hyperparameters, then export
  the tree’s structure.

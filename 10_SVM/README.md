# Support Vector Machines

**Support Vector Machines** (SVMs) is one of the most powerful machine learning models. On small amounts of data, it may even outperform Neural Networks. So let’s explore what its power consists of.

## Selected Dataset

Heart Disease Dataset. Available [here](https://bit.ly/3Nkw8fd).

## Tasks

For this chapter, you will have to do the following:

- Import the Data Set.
- Firstly, we will explore how the feature scale influences the algorithm's performance. Train an SVM model on 4 versions of the Data Set:
  - The initial one.
  - The one passed through the StandardScaler.
  - The one passed through the MinMaxScaler.
  - The one passed through the MaxAbsScaler.
    Create the following table in pandas and compare the results. Comment them:

| Initial | standard_scaler | min_max_scaler | max_abs_scaler |
| ------- | --------------- | -------------- | -------------- |
| ‎       |                 |                |                |

- Usually, SVMs use some Kernel to move the data to another space where linear planes separate the classes. In this task, you will have to explore how different kernels influence the decision boundary. Create the plots of decision boundary for the following kernels:
  - linear
  - poly
  - rbf
  - sigmoid

Plot them all together in a combined plot, compare them, and express some conclusions.

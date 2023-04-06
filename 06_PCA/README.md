# Principal Component Analysis (PCA)

Till now, you learned 2 algorithms for supervised Machine Learning. However, in the real world, labeled data is very expensive. It often costs a lot for a company to get labeled data, and they are asked to work with the unlabeled one and extract hints and insights from it.
In this task, we invite you to explore one of the types of unsupervised learning - **Dimensional Reduction**.

This task is made up of 2 subtasks.

## Subtask 1

In the first, you are going to work with the Iris Data Set.

- Load the Data Set from [here](https://bit.ly/3WiUJ7W).
- Plot the first 3 columns of the Data Set and the target column in a 3d scatter plot.
  HINT: Use the target column as a hue for the points.
  LINK: (https://bit.ly/3SRIsEJ)
- Copy the implementation of the Principal Component Analysis algorithm from SMLH.
- Create an instance of the Scratch-made PCA algorithm using the eigenvector algorithm.
- Create an instance of the Scratch-made PCA algorithm using the SVD algorithm.
- Create an instance of sklearn and implement a PCA algorithm.
- Apply StandardScaler from sklearn on the data.
- Train all created instances of PCA on the iris data.
- Use each created instance of PCA to reduce the dimensionality of the Data Set to 2, creating in such a way 3 separated Data Sets.
- Create a plot that combines 3 scatter plots and plots each of the result Data Sets in a separate window. Each window should be related to which version of the PCA was used.
  HINT: (https://bit.ly/3DIzAwW)
- Try to conclude what you see by comparing the results of each algorithm and the 3d scatter plot you made before.
- Retrain a sklearn PCA model on the iris Data Set with _n_components_ set to 1.
- Create a line plot of the _explained_variance_ratio_.
- Try to make a conclusion based on that plot.

## Subtask 2

In the second task, you will work with another Data Set - images of digits:

- First, load the Data Set from [here](https://bit.ly/3SOwFqL).
- Second plot in a multiple window plot 10 random digits with a title having the digit from the image on a 2 x 5 grid.
- Create an instance of the sklearn PCA.
- Apply scaling on the digit Data Set.
- Train the PCA on the digit Data Set.
- Reduce the dimensionality of the Data Set to 2 dimensions.
- Plot the new result Data Set in a scatter plot with each point colored by its digit label.

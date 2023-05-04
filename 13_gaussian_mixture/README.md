# Gaussian Mixture Models. EM algorithm. KMeans

You already got to know the clustering problem in Machine Learning. Also, you met one of the business problems where these algorithms are used - customer segmentation. Today you are going to practice this knowledge on a very similar task.

## Selected Data Set

Wine Customer Segmentation Data Set. Available [here](https://bit.ly/3Nn242k).

## Tasks

For this chapter, you will have to do the following:

- Bring all columns into a numeric form: applying mapping or dummy variables.
- If you think it can be helpful, you may apply feature scaling.
- Using Silhouette score, find the best number of clusters for GMM (implemented in sklearn.)
- Using Silhouette score, find the best number of clusters for KMeans (implemented in sklearn.)
- Plot the process of choosing the best number of clusters for each algorithm and try to explain.
- Cluster the Data Set using both algorithms.
- Extract from the KMeans algorithm the centroids.
- Extract from GMM the means of the clusters.
- Build the following table for both algorithms, and fill the table with the means of the clusters.

|           | feature 1 | feature 2 | ... | feature m |
| --------- | --------- | --------- | --- | --------- |
| cluster 1 |           |           |     |           |
| cluster 2 |           |           |     |           |
| ...       |           |           |     |           |
| cluster n |           |           |     |           |

- Make a conclusion based on the table you got and create an imaginary customer for every cluster.

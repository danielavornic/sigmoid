import numpy as np
from sklearn.preprocessing import StandardScaler


class PCA_eigenvector:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components_ = None

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

    def fit(self, X):
        cov_mat = np.cov(X.T)
        eig_vals, eig_vecs = np.linalg.eig(cov_mat)
        eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:, i])
                     for i in range(len(eig_vals))]
        eig_pairs.sort(key=lambda x: x[0], reverse=True)

        matrix_w = np.hstack((eig_pairs[i][1].reshape(
            np.size(X, 1), 1) for i in range(self.n_components)))

        self.components_ = matrix_w

    def transform(self, X):
        X_std = StandardScaler().fit_transform(X)
        return np.dot(X_std, self.components_)


import numpy as np


class LogisticRegression:
    def __init__(self, learning_rate: float = 0.05, max_inter: int = 100000) -> None:
        '''
        The constructor of the Logistic Regression model.
            :param learning_rate:float, default=0.05
                The learning rate of the model
            :param max_inter: int, default = 100000
                The number of iteration to go throw

        '''
        # Setting use of the hyperparameters
        self.__learning_rate = learning_rate
        self.__max_inter = max_inter

    def sigmoid(self, y: 'np.array') -> 'np.array':
        '''
        The sigmoid function
            :param y: np.array
                The predictions of the linear function
        '''
        return 1 / (1 + np.exp(-y))

    def fit(self, X: 'np.array', y: 'np.array') -> LogisticRegression:
        '''
            The fit function of the model.
                :param X: 2-d np.array
                    The matrix with the features.
                :param y: 1-d np.array
                    The target vector
        '''
        # Creating the weights vector
        self.coef_ = np.zeros(len(X[0] + 1))

        # Adding the intercept column
        X = np.hstack((X, np.ones((len(x), 1))))

        # The weights updating process:
        for i in range(self.__max_iter):
            # Prediction
            pred = self.sigmoid(np.dot(X, self.coef_))

            # Coputing the gradient
            gradient = np.dot(X.T, (pred - y)) / y.size

            # Updating the weights
            self.coef_ -= gradient * self.__learning_rate

        return self

    def predict_proba(self, X: 'np.array') -> 'np.array':
        '''
        This function returns the class probabilities
            :param X: 2-d np.array
                The features matrix
            :return: 2-d, np.array
                The array with the probabilities for every class for every sample
        '''
        # Adding the intercept column
        X = np.hstack((X, np.ones((len(X), 1))))

        # Computing the probabilites
        prob = self.sigmoid(np.dot(X, self.coef_))

        # Returning the probabilities
        return np.hstack(((1 - prob).reshape(-1, 1), prob.reshape(-1, 1)))

    def predict(self, X: 'np.array') -> 'np.array':
        '''
        This funciton returns the predictions of the model
            :param X: 2-d np.array
                The features matrix
            :return: 2-d, np.array
                The array with the probabilities for every class for every sample
        '''
        # Adding the intercept column
        X = np.hstack((X, np.ones((len(X), 1))))
        return (self.sigmoid(np.dot(X, self.coef_)) > 0.5) * 1

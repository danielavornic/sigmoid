import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


def nulls_table(df):
    nulls = df.isnull().sum()
    percent = round(df.isnull().sum() / len(df) * 100, 2)
    nulls = nulls[nulls != 0]
    percent = percent[percent != 0]
    return pd.concat([nulls, percent], axis=1, keys=['nulls', '%'])


def to_numeric(df, col):
    df[col] = df[col].astype('category').cat.codes
    return df


def outliers(df, col):
    """
    Detects and returns the outliers in a given column of a dataframe based on the interquartile range (IQR) method.

    Args:
        df (pandas.DataFrame): The dataframe containing the data.
        col (str): The name of the column for which outliers are to be detected.

    Returns:
        pandas.DataFrame: A subset of the original dataframe containing the outliers.
    """

    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    return df[(df[col] < lower_bound) | (df[col] > upper_bound)]


def evaluate_model(y_test, y_pred):
    print('Classification Report:')
    print(classification_report(y_test, y_pred))
    print('Accuracy Score:')
    print(accuracy_score(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()

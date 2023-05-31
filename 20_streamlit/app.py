import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)
import shap
from streamlit_shap import st_shap

shap.initjs()
base_dir = os.path.dirname(os.path.abspath(__file__))


@st.cache_data
def load_data():
    data_path = os.path.join(base_dir, 'data', 'wine.csv')
    data = pd.read_csv(data_path)
    return data


def load_cover_image():
    image_path = os.path.join(base_dir, 'dataset_cover.jpg')
    image = plt.imread(image_path)
    return image


def home():
    st.title("Wine Quality Dataset")

    image = load_cover_image()
    st.image(image, use_column_width=True)

    st.header("Description")

    st.write("This dataset is related to red variants of the Portuguese 'Vinho Verde' wine. The dataset describes the amount of various chemicals present in wine and their effect on its quality. The datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones). Your task is to predict the quality of wine using the given data.")
    st.write("A simple yet challenging project, to anticipate the quality of wine. The complexity arises due to the fact that the dataset has fewer samples and is highly imbalanced. Can you overcome these obstacles and build a good predictive model to classify them?")

    st.header("Attribute Information")
    st.subheader("Input variables (based on physicochemical tests):")
    st.write("1 - fixed acidity")
    st.write("2 - volatile acidity")
    st.write("3 - citric acid")
    st.write("4 - residual sugar")
    st.write("5 - chlorides")
    st.write("6 - free sulfur dioxide")
    st.write("7 - total sulfur dioxide")
    st.write("8 - density")
    st.write("9 - pH")
    st.write("10 - sulphates")
    st.write("11 - alcohol")
    st.subheader("Output variable (based on sensory data):")
    st.write("12 - quality (score between 0 and 10)")

    st.header("Acknowledgements:")
    st.write(
        "This dataset is also available from Kaggle & UCI machine learning repository, [link](https://archive.ics.uci.edu/ml/datasets/wine+quality).")


def data_exploration(data):
    st.title('Data Exploration & Visualization')

    st.header('Data Information')
    st.dataframe(data.head())

    data = data.drop('Id', axis=1)

    st.dataframe(data.describe())

    st.header('Correlation Matrix')
    corr_matrix = data.corr()
    st.write(corr_matrix)

    st.header('Correlation Heatmap')
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    st.pyplot(fig)

    st.header('Quality Distribution')
    quality_counts = data['quality'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=quality_counts.index, y=quality_counts.values)
    plt.xlabel('Quality')
    plt.ylabel('Count')
    st.pyplot(fig)

    st.header('Alcohol vs. Quality')
    fig, ax = plt.subplots()
    sns.boxplot(x='quality', y='alcohol', data=data)
    plt.xlabel('Quality')
    plt.ylabel('Alcohol')
    st.pyplot(fig)


def model_training(data):
    st.title('Model Training')

    st.header('Model Description')
    st.markdown('**Random Forest Classifier** is an ensemble learning method for classification. A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is controlled with the `max_samples` parameter if `bootstrap=True` (default), otherwise the whole dataset is used to build each tree.')

    st.header('Input Parameters')
    cols = data.columns[:-2].tolist()
    selected_cols = st.multiselect('Select columns', cols, cols)
    use_default_params = st.checkbox('Use Default Parameters', value=True)
    if use_default_params:
        bootstrap = True
        max_depth = None
        n_estimators = 100
        criterion = 'gini'
        min_samples_split = 2
        min_samples_leaf = 1
        max_leaf_nodes = 50
        random_state = 42
    else:
        bootstrap = st.selectbox(
            'Bootstrap', [True, False], index=0, key='bootstrap', help='Whether bootstrap samples are used when building trees')
        max_depth_option = st.radio(
            'Max Depth', ['None', 'Integer'], key='max_depth_option', horizontal=True)
        if max_depth_option == 'None':
            max_depth = None
        else:
            max_depth = st.slider('Max Depth', min_value=2,
                                  max_value=50, value=10, help='The maximum depth of the tree')
        n_estimators = st.slider('Number of Estimators',
                                 min_value=10, max_value=1000, value=100, help='The number of trees in the forest')
        criterion = st.selectbox(
            'Criterion', ['gini', 'entropy', 'log_loss'], index=0, help='The function to measure the quality of a split')
        min_samples_split = st.slider('Min Samples Split',
                                      min_value=2, max_value=30, value=2, help='The minimum number of samples required to split an internal node')
        min_samples_leaf = st.slider('Min Samples Leaf',
                                     min_value=1, max_value=20, value=1, help='The minimum number of samples required to be at a leaf node')
        max_leaf_nodes = st.slider('Max Leaf Nodes',
                                   min_value=10, max_value=100, value=50, help='Grow trees with max_leaf_nodes in best-first fashion')
        random_state = st.number_input(
            'Random State', value=42, help='The seed used by the random number generator')

    st.header('Model Training')
    if st.button('Train Model'):
        X = data[selected_cols]
        y = data['quality']
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=random_state)

        model = RandomForestClassifier(
            bootstrap=bootstrap,
            max_depth=max_depth,
            n_estimators=n_estimators,
            criterion=criterion,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            max_leaf_nodes=max_leaf_nodes,
            random_state=random_state
        )
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        with st.container():
            st.header('Model Parameters')
            st.write('Selected columns:', selected_cols)
            st.write('Max Depth:', max_depth)
            st.write('Number of Estimators:', n_estimators)
            st.write('Criterion:', criterion)
            st.write('Min Samples Split:', min_samples_split)
            st.write('Min Samples Leaf:', min_samples_leaf)
            st.write('Max Leaf Nodes:', max_leaf_nodes)
            st.write('Random State:', random_state)

        st.header('Model Evaluation')
        st.write('Accuracy:', accuracy_score(y_test, y_pred))
        st.write('F1 Score:', f1_score(y_test, y_pred, average='weighted'))
        st.write('Precision:', precision_score(
            y_test, y_pred, average='weighted'))
        st.write('Recall:', recall_score(y_test, y_pred, average='weighted'))

        st.header('Feature Importance')
        feature_importance = pd.Series(
            model.feature_importances_, index=selected_cols)

        fig, ax = plt.subplots()
        sns.barplot(x=feature_importance.index,
                    y=feature_importance.values, ax=ax, palette='Reds')
        ax.set_xlabel('Features')
        ax.set_ylabel('Importance')
        ax.set_xticklabels(feature_importance.index, rotation=90)
        ax.legend().remove()
        st.pyplot(fig)

        st.header('SHAP Analysis')

        with st.spinner('Generating SHAP values and plots...'):
            explainer = shap.Explainer(
                model.predict, X_train, feature_names=X.columns)
            shap_values = explainer(X_test)

        st.subheader('SHAP Summary Plot')
        st_shap(shap.plots.beeswarm(shap_values), height=350)

        st.subheader('SHAP Bar Plot')
        st_shap(shap.plots.bar(shap_values), height=350)

        st.subheader('SHAP Waterfall Plot for the First Prediction')
        st_shap(shap.plots.waterfall(shap_values[0]), height=350)


def main():
    st.set_page_config(page_title='Wine Quality Dataset',
                       page_icon=':wine_glass:')
    with st.sidebar:
        st.title('Navigation')
        page = st.radio('Go to', ('Home', 'Data Exploration & Visualization',
                        'Model Training'), index=0, key='nav')

    data = load_data()

    if page == 'Home':
        home()
    elif page == 'Data Exploration & Visualization':
        data_exploration(data)
    elif page == 'Model Training':
        model_training(data)


if __name__ == '__main__':
    main()

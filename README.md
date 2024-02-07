######
# Road Traffic Accidents Severity Prediction

## Overview

This repository contains the code for our project **Road Traffic Accidents Severity Prediction**, which was developed as part of our [Data Scientist training](https://datascientest.com/en/data-scientist-course) at [DataScientest](https://datascientest.com/).

### Objectives

The primary objective of this project is to develop a precise predictive model capable of estimating the severity of road traffic accidents in France using historical data. By analyzing data spanning from 2018 to 2021, we will clean and preprocess the data, extract relevant features, and build predictive models. We will test various models and evaluation methods to identify the most effective approach. The final model will be trained on historical data.

Our ultimate goal is to provide insights that can support targeted prevention and intervention measures, contributing to a reduction in the number of severe accidents on French roads.

### Team

This project was developed by the following team members:

- Artem    ([GitHub] (https://github.com/artmskfr)/ [LinkedIn](http://linkedin.com/))
- Fabien   ([GitHub](https://github.com/Henri35/)/[LinkedIn](http://linkedin.com/))
- Jerome   ([GitHub](https://github.com/Jeromik/)
- Juliette [GitHub](https://github.com/JulietteB927/)/[LinkedIn](http://linkedin.com/))

### Contents

- **Folder 1: Modélisation** - Contains Jupyter notebooks for each algorithm and for both binary and multiclass cases. Additionally, there are folders containing saved results of algorithm runs.

- **Folder 2: EDA (Exploratory Data Analysis)** - Includes Jupyter notebooks for data preprocessing, specific to each initial dataset.

- **Folder 3: Data** - Contains all the initial datasets used in this project.

- **Fusion_Pre-processing_for_model.ipynb** - This notebook includes all the code for data preprocessing and dataset preparation for the modeling phase.
#####

You will need to install the dependencies (in a dedicated environment) :

```
pip install -r requirements.txt
```

## Streamlit App

**Add explanations on how to use the app.**

To run the app (be careful with the paths of the files in the app):

```shell
conda create --name my-awesome-streamlit python=3.9
conda activate my-awesome-streamlit
pip install -r requirements.txt
streamlit run app.py
```

The app should then be available at [localhost:8501](http://localhost:8501).

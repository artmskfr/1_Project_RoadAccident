import os
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import joblib
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import plotly.express as px
from sklearn.model_selection import train_test_split

title = "Évaluation (démo)"
sidebar_name = "Évaluation (démo)"

MODELS_PATHS = {
    "Binaire": "streamlit_app/assets/modele_binaire",
    "Multiclasse": "streamlit_app/assets/modele_multiclasse"
}

def load_data(mode):
    dff = pd.read_csv("data/dataset_18-21_for_model_encoding.csv", sep=',', index_col=0)
    X = dff.drop(['grav'], axis=1)
    y = dff['grav']

    if mode == "Binaire":
        y = y.replace([1, 4], 0).replace([2, 3], 1)

    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_test, y_test

def evaluate_selected_model(mode, model_name):
    X, y = load_data(mode)  # Charger X_test et y_test
    
    model_path = os.path.join(MODELS_PATHS[mode], model_name)
    model = joblib.load(model_path)
    predictions = model.predict(X)

    target_names = ["classe 0", "classe 1"] if mode == "Binaire" else ["Indemne", "Tué", "Blessé", "Blessé léger"]
    report_dict = classification_report(y, predictions, target_names=target_names, output_dict=True)

    return pd.DataFrame(report_dict).transpose(), X, y, model, predictions

def visualize_metric(report_df, chosen_metric):
    fig = px.bar(report_df, x=report_df.index, y=chosen_metric, labels={'x':'Classe', 'y':chosen_metric.capitalize()}, title=f"{chosen_metric.capitalize()} par classe")
    fig.update_layout(autosize=True)
    st.plotly_chart(fig)

def run(image_width):
    st.title(" Évaluation des modèles")

    mode_evaluation = st.selectbox("Choisissez le mode d'évaluation", ["Binaire", "Multiclasse"])
    modeles_disponibles = os.listdir(MODELS_PATHS[mode_evaluation])
    selected_model_name = st.selectbox("Choisissez un modèle pour la prédiction", modeles_disponibles)

    if st.button('Évaluer le modèle'):
        report_df, X, y, model, predictions = evaluate_selected_model(mode_evaluation, selected_model_name)
        st.session_state.report_df = report_df
        st.session_state.X = X
        st.session_state.y = y
        st.session_state.model = model
        st.session_state.predictions = predictions

    if "report_df" in st.session_state:
        st.dataframe(st.session_state.report_df)  # Afficher le rapport de classification à partir de session_state
        metrics = ['precision', 'recall', 'f1-score']
        chosen_metric = st.selectbox("Choisissez une métrique à visualiser", metrics)
        visualize_metric(st.session_state.report_df, chosen_metric)
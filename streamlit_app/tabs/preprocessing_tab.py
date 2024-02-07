import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report



title = "Pre-processing & feature engineering"
sidebar_name = "Pre-processing & feature engineering"

# *********************************************************************************************************************************************************** #
def run(image_width):

    # st.title(title)

    sections = ["Réduction des variables", "Analyse des variables", "Gestion des Nan", "Regroupement et ajout de variables (1/2)", "Regroupement et ajout de variables (2/2)", "Pipeline de préparation des données"]

    # Navigation avec des boutons radio    
    # st.markdown("## Sommaire")
    selected_section = st.radio("", sections)

    # Affiche le contenu en fonction de la section choisie
    if selected_section == "Réduction des variables":
        st.header("Réduction des variables")
        st.markdown("---")
        st.write("Les sections suivantes, qui vont être détaillées, ont permis de réduire le nombre de variables à considérer pour notre problématique")
        st.image("streamlit_app/assets/prepro_1.jpg", caption='', width=854)

    elif selected_section == "Analyse des variables":
        st.header("Analyse des variables")
        st.markdown("---")
        st.write("Exemple d'analyse des variables sur le dataset des véhicules")
        st.image("streamlit_app/assets/prepro_2.jpg", caption='', width=1169)

    elif selected_section == "Gestion des Nan":
        st.header("Gestion des Nan")
        st.markdown("---")
        st.write("Gestion par : 1 - Suppression de colonne, 2 - Suppression de lignes, 3 - Remplacement par la modalité")
        st.image("streamlit_app/assets/prepro_3.jpg", caption='', width=1400)


    elif selected_section == "Regroupement et ajout de variables (1/2)":
        st.header("Variables supplémentaires et regroupement de catégories")
        st.markdown("---")
        st.write("Variables nouvelles, par création/regroupement :")
        st.code(""" 
        Nb_veh 	        - Nombre total des véhicule appliquée dans l’accident
        age_cond 	- Age des conducteurs
        age_usag 	- Age des usagers
        sexe_cond	- Sexe des conducteurs
        periode 	- Moment de la journée de l’accident
        week end 	- Accident le weekend ou en semaine""")
        st.image("streamlit_app/assets/prepro_4.jpg", caption='', width=1278)

    elif selected_section == "Regroupement et ajout de variables (2/2)":
        st.header("Exemple d'ajout de la variable : Nb_veh")
        st.markdown("---")
        st.image("streamlit_app/assets/prepro_5.jpg", caption='', width=1297)
        st.write("""
                - L'analyse permet de voir que les accidents de plus de 10 voitures sont rares, et que la majorité implique 2 véhicules. 80% des accidents comportent 2, 3 ou 4 véhicules.
                - En même temps, la nouvelle variable Nb_veh met en évidence que la gravité est plus importante lorsque l'accident ne comporte qu'un seul véhicule (29 est une aberration statistique).
                - La création de cette nouvelle variable est donc justifiée, car elle met en évidence une information cachée qui impacte la valeur de sortie, la cible.
                 """)


    elif selected_section == "Pipeline de préparation des données":
        st.header("Pipeline de préparation des données")
        st.markdown("---")
        st.write("""
                 Une analyse des variables a permis de :
                 - Réduire le nombre de variables
                 - Créer de nouvelle variables pertinentes

                 Les traitements suivants furent :
                 - L'encodage par get_dummies
                 - La gestion du rééquilibrage des classes
                 - L'utilisation d'un ratio 80/20 pour les jeux de d'entrainement et de test
                 """)


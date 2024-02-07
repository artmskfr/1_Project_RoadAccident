import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

import plotly.io as pio
pio.renderers.default = 'notebook'


title = "Présentation des données"
sidebar_name = "Présentation des données"


def dataset_usagers():
   
    df_propre = pd.read_csv("data/dataset_18-21_usagers_propre.csv")

    feature_x = st.selectbox("Which feature on x?", df_propre.columns, index =3)
    feature_y = st.selectbox("Which feature on y?", df_propre.columns, index=2)

    label_X=[]
    label_y=[]

    lab_gravite = dict({1 : 'Indemne',  4 : 'Blessé léger', 3 : 'Blessé hospitalisé', 2 : ' Tué'})
    lab_place = dict({1 : "place conducteur", 2 : "place du mort", 3 : "autre"})
    lab_catu = dict({ 1 : "conducteur", 2 : "passager", 3 : "piéton"})
    lab_sexe = dict({1 : "Homme", 2 : "Femme"})
    lab_trajet = dict({1 : 'Domicile-Travail', 2 : 'Promenade loisir', 3 : ' Autres'})
    lab_secu1 = dict({1 : 'Ceinture', 2 : ' Casque', 3 : 'Non déterminable', 4 : 'Autre'})

    if(feature_x == "grav") : label_X = lab_gravite
    if(feature_x == "place") : label_X = lab_place
    if(feature_x == "catu") : label_X = lab_catu
    if(feature_x == "sexe_usag") : label_X = lab_sexe
    if(feature_x == "trajet") : label_X = lab_trajet
    if(feature_x == "secu1") : label_X = lab_secu1

    if(feature_y == "grav") : label_y = lab_gravite
    if(feature_y == "place") : label_y = lab_place
    if(feature_y == "catu") : label_y = lab_catu
    if(feature_y == "sexe_usag") : label_y = lab_sexe
    if(feature_y == "trajet") : label_y = lab_trajet
    if(feature_y == "secu1") : label_y = lab_secu1


    st.write('Visualiser hist de variable')
    label_X_df = pd.DataFrame.from_dict(label_X, orient='index')
    fig = px.bar(df_propre[feature_x].value_counts())
    fig.update_traces(showlegend=True)
    fig.update_layout(yaxis=dict(title=''),
                xaxis=dict(title='',
                gridcolor='grey',
                tickvals = label_X_df.index, 
                ticktext = label_X_df[0])
                )
    st.plotly_chart(fig)
        
    
    agree = st.checkbox('Visualiser croisement variable', key ="two")
    if agree:

        label_X_df = pd.DataFrame.from_dict(label_X, orient='index')
        label_y_df = pd.DataFrame.from_dict(label_y, orient='index')

        df = pd.crosstab(df_propre[feature_x], df_propre[feature_y])
        fig = px.bar(df)

        fig.update_traces(showlegend=True)
        fig.update_layout(      
            xaxis=dict(title='',
            gridcolor='grey',
            tickvals = label_X_df.index, 
            ticktext = label_X_df[0])
            )
        st.plotly_chart(fig)


def run(image_width):

    sections = ["Présentation du jeu de données", "Variables du jeu de données", "Exemple : Dataset Usager"]

    # Navigation avec des boutons radio    
    # st.markdown("## Sommaire")
    selected_section = st.radio("", sections)

    # Affiche le contenu en fonction de la section choisie
    if selected_section == "Présentation du jeu de données":
        st.header("Présentation du jeu de données")
        st.markdown("---", unsafe_allow_html=True)
    
        st.markdown(
        """
Le jeux de données dans le cadre de ce projet est une base de données d’accidents corporels de la
circulation routière disponible sur site data.gouv.fr ( web ). Cette base est constituée annuellement de plusieurs
fichiers. Les données utilisées dans le projet portent sur la période 2018-2021 uniquement. Ces données sont
produites par le ministère de l’intérieur, et sont disponibles librement (licence ouverte).
Le jeu de données est réparti en quatres rubriques sous forme de fichiers au format csv :
• CARACTERISTIQUES qui décrit les circonstances générales de l’accident
• LIEUX qui décrit le lieu principal de l’accident
• VEHICULES impliqués
• USAGERS impliqués.""")
    
        st.image("streamlit_app/assets/relations.jpg", caption='Schéma relationnel des données', width=1084)

        st.image("streamlit_app/assets/dataframe.jpg", caption='Extrait de dataframe', width=1312)

        # st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

    elif selected_section == "Variables du jeu de données":
        st.header("Variables du jeu de données")
        st.markdown("---", unsafe_allow_html=True)

        st.code(""" Nombre initial de variables : 
                11 - Véhicules
                18 - Lieux
                17 - Caractéristiques
                16 - Usagers""")

        st.image("streamlit_app/assets/vars.jpg", caption='', width=1342) 

    elif selected_section == "Exemple : Dataset Usager":
        st.header("Exemple : Dataset Usager")
        st.markdown("---", unsafe_allow_html=True)

        dataset_usagers()


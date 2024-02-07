import streamlit as st


title = "Accidents de la route"
sidebar_name = "Contexte & objectifs"


def run(image_width):

    st.title(title)
    st.markdown("---")

    sections = ["Contexte", "Objectifs"]

    # Navigation avec des boutons radio    
    # st.markdown("## Sommaire")
    selected_section = st.radio("", sections)

    # Affiche le contenu en fonction de la section choisie
    if selected_section == "Contexte":
        st.header("Contexte")
        col1, col2 = st.columns([1,1])
        with col1:          
            st.image('streamlit_app/assets/etat.jpg', width=700)
        with col2:
            st.code("""Les dépenses de l'Etat pour la sécurité routière : 
    - 273 M€ pour améliorer le réseau routier et sa sécurité
    - 145 M€ pour les projets sécurité routière des collectivités territoriales
    - 316 M€ pour le bon fonctionnement du contrôle automatique
    - 26 M€ pour améliorer la prise en charge des blessés de la route.""")

    elif selected_section == "Objectifs":
        st.header("Objectifs")
        col1, col2 = st.columns([1,1])
        with col1:
            st.image('https://i.gifer.com/XJ0y.gif', caption='Ouille', width=600)
        with col2:
            st.write("""
L'objectif principal de ce projet est de développer un modèle prédictif précis qui peut estimer la gravité
des accidents routiers en France se basant sur les données historiques.""")
   
            st.write("""
En utilisant les données historiques sur la période de 2018 - 2021, nous allons nettoyer et préparer les
données, extraire les caractéristiques les plus pertinentes, puis créer un modèle prédictif. Nous allons tester
différents modèles et méthodes d'évaluation pour trouver l'approche la plus performante. Le modèle final sera
entraîné sur les données historiques.
        """)
    
            st.write("""
L'objectif final est de fournir des informations pour pouvoir prendre des mesures de prévention et
d'intervention ciblées, contribuant ainsi à la réduction du nombre d'accidents graves sur les routes françaises.
        """)
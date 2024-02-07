import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


title = "Impact des variables & optimisation des résultats"
sidebar_name = "Impact des variables & optimisation des résultats"


def run(image_width):

    sections = ["Impact des variables", "Impact des variables - Shap","Optimisation des résultats 1/2", "Optimisation des résultats 2/2"]

    # Navigation avec des boutons radio    
    # st.markdown("## Sommaire")
    selected_section = st.radio("", sections)

    # Affiche le contenu en fonction de la section choisie
    if selected_section == "Impact des variables":
        st.header("Impact des variables")
        st.markdown("---", unsafe_allow_html=True)

        col1, col2 = st.columns([1,1])
        
        col1, col2 = st.columns([1,1])
        with col1:          
            st.image('streamlit_app/assets/shap_1.jpg', caption = "Les 30 caractéristiques les plus importantes pour Random Forest", width=763)
        with col2:
            st.image('streamlit_app/assets/shap_2.jpg', caption = "Rapports de classification pour différentes quantités de variables", width=763)
        

    elif selected_section == "Impact des variables - Shap":
        st.header("Impact des variables - Shap")
        st.markdown("---", unsafe_allow_html=True)

        col1, col2 = st.columns([1,1])
        with col1:          
            st.image('streamlit_app/assets/shap_global_1.png', caption = "Le diagramme shap", width=763)
        with col2:
            st.image('streamlit_app/assets/shap_global_2.png', caption = "Évaluation de l'impact moyen des caractéristiques", width=763)

    
    elif selected_section == "Optimisation des résultats 1/2":
    
        st.header("Optimisation des résultats")
        st.markdown("---", unsafe_allow_html=True)

        

        _, col2, _ = st.columns([1,3,1])
        with col2:  
            st.image('streamlit_app/assets/optim_3.jpg', caption = "", width=753)
            st.markdown("\n\n")

        col4, col5 = st.columns([1,1])
        with col4:
            st.markdown("###### Rapport de classification (seuil 0.5) : ")          
            st.image('streamlit_app/assets/optim_1.jpg', caption = "Random Forest, rapport de classification - cas binaire", width=485)
        with col5:
            st.markdown("###### Rapport de classification (seuil 0.4) : ")
            st.image('streamlit_app/assets/optim_2.jpg', caption = "Random Forest, rapport de classification - Seuil de 0,4", width=490)


    
    
    elif selected_section == "Optimisation des résultats 2/2":
        st.header("Optimisation des résultats")
        st.markdown("---", unsafe_allow_html=True)

        _, col2, _ = st.columns([1,3,1])
        with col2:  
            st.markdown("<div style='text-align: left;'><h6>Résultats de prédictions pour différents seuils : </h6></div>", unsafe_allow_html=True)
            st.image('streamlit_app/assets/optim_6.jpg', caption = "Résultats de prédictions pour différents seuils", width=900)
            
            st.markdown("\n\n\n")

        col4, col5 = st.columns([1,1])
        with col4:
            st.markdown("###### Rapport de la classification et Matrice de confusion pour le seuil de probabilité de 0.28 : ")
            
            st.image('streamlit_app/assets/optim_4_1.jpg', width=220)
            st.markdown("\n\n")
            #st.image('streamlit_app/assets/optim_4.jpg', caption = "Random Forest, Rapport de la classification pour le seuil de probabilité de 0.28", width=700)
            st.markdown("###### Rapport de la classification :")
            st.image('streamlit_app/assets/optim_4.jpg', width=500)
        with col5:
            st.markdown("###### Rapport de la classification et Matrice de confusion pour le seuil de probabilité de 0.40")
        
            st.image('streamlit_app/assets/optim_5_1.jpg', width=200)
            #st.markdown("\n")
            
            st.markdown("###### Rapport de la classification :")
            st.image('streamlit_app/assets/optim_5.jpg', width=450)
            
            
            #st.image('streamlit_app/assets/optim_5.jpg', caption = "Random Forest, Rapport de la classification pour le seuil de probabilité de 0.40", width=700)




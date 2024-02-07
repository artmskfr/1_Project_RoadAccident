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


title = "Modélisation Méthodologie"
sidebar_name = "Modélisation Méthodologie"


def load_data_from_csv_multi():
    dff = pd.read_csv("data/dataset_18-21_for_model_encoding.csv", sep=',', index_col=0)
    X = dff.drop(['grav'], axis=1)
    y = dff['grav']
    return X, y

def load_data_from_csv_binary():
    dff = pd.read_csv("data/dataset_18-21_for_model_encoding.csv", sep=',', index_col=0)
    X = dff.drop(['grav'], axis=1)
    y = dff['grav']
    y = y.replace([1, 4], 0).replace([2, 3], 1)
    return X, y

def get_class_percentages(y):
    mapping = {
    1: "Indemne",
    2: "Tué",
    3: "Blessé",
    4: "Blessé léger"}
    y = y.replace(mapping)
    class_percentages = (y.value_counts(normalize=True) * 100).reset_index()
    class_percentages.columns = ['Classe', 'Pourcentage']
    class_percentages['Pourcentage'] = class_percentages['Pourcentage'].apply(lambda x: f"{x:.2f}%")
    return class_percentages


def get_class_percentages_binary(y):
    mapping = {
    0: "Pas grave",
    1: "Grave"}
    y = y.replace(mapping)
    class_percentages = (y.value_counts(normalize=True) * 100).reset_index()
    class_percentages.columns = ['Classe', 'Pourcentage']
    class_percentages['Pourcentage'] = class_percentages['Pourcentage'].apply(lambda x: f"{x:.2f}%")
    return class_percentages


# *********************************************************************************************************************************************************** #
def run(image_width):
    
    # st.title(title)

    sections = ["Cas binaire et multiclasse", "Métriques", "Gestion de l’échantillonnage", "Synthèse des résultats"]

    # Navigation avec des boutons radio    
    # st.markdown("## Sommaire")
    selected_section = st.radio("", sections)

    # Affiche le contenu en fonction de la section choisie
    if selected_section == "Cas binaire et multiclasse":
        st.header("Cas binaire et multiclasse")
        st.markdown("---")
        col1, col2 = st.columns([1,1])
        with col1:          
            st.image('streamlit_app/assets/casmulti.jpg', width=591)
        with col2:
            st.code("""
                    Le cas multiclasse offre une analyse plus nuancées, 
    mais les données présentent un fort déséquilibre :
                    
    - 1 = Indemne               > 42,5 %
    - 2 = Tué                   >  2,6 %
    - 3 = Blessé hospitalisé    > 15,8 %
    - 4 = Blessé léger          > 39,2 %
                    """)
        col3, col4 = st.columns([1,1])
        with col3:          
            st.image('streamlit_app/assets/casbin.jpg', width=561)
        with col4:
            st.code("""
                    Le cas binaire permet une analyse plus simple et un réquilibrage partiel, 
    mais il perd les nuances offertes par le multiclasse :
                    
    - 0 = Pas grave               > 81,7 %
    - 1 = Grave                   > 18,3 %
                    """)

    elif selected_section == "Métriques":
        st.header("Métriques")
        st.markdown("---")
        
        col1, col2 = st.columns([1,1])
        with col1:
            st.image('streamlit_app/assets/matconf.jpg', caption='Matrice de confusion', width=704)
        with col2:
            st.write("")
            st.code("""
Métriques utilisées : 

- F score ( Fbeta score, Weighted F1, Macro F1)
                    
- Matthews coefficient
                    
- AUC & ROC
                    
- Métrique personnelle : 
            Par exemple : f1_class2, 
                          (1.5 * f1_classe2 + f1_classe3) / 2.5
                    """)
      

    elif selected_section == "Gestion de l’échantillonnage":
        st.header("Gestion de l’échantillonnage")
        st.markdown("---")
        st.image('streamlit_app/assets/echan.jpg', caption="Résultats avec différentes méthodes de gestion de l'échantillonnage", width=1359)
        st.markdown(""" ##### Un jeu de données déséquilibré peut introduire des biais dans les prédictions""")
        st.write(""" •	Afin d'améliorer la qualité de nos prédictions, nous avons testé des plusieurs techniques de rééqulibrage des classes.""")
        st.write(""" •	Deux types de techniques se distinguent :""")
        st.markdown("""\t\t\t\t **Balanced** : Ajuste le poids de chaque classe pour équilibrer leur influence sans modifier l'ensemble des données.""", unsafe_allow_html=True)
        st.markdown("""\t\t\t\t **Oversampling et Undersampling** : Ajustent la distribution des classes en augmentant ou réduisant les populations de certaines d'entre elles.""", unsafe_allow_html=True) 
        st.write("""""")
        st.write(""" •	La méthode "Balanced" (Meth_5) et a été retenue pour sa capacité à harmoniser la distribution des classes tout en prévenant le surapprentissage""")

    elif selected_section == "Synthèse des résultats":
        st.header("Synthèse des résultats")
        st.markdown("---")

        _, col2, _ = st.columns([1,3,1])
        _, col5, _ = st.columns([1,3,1])
        with col2:          
            #st.image('streamlit_app/assets/synth_1.jpg', caption="Synthèse des résultats en multiclasse", width=929)
            
            st.markdown("<p style='font-weight: bold; font-size: 20px; text-align: left;'>Synthèse des résultats en multiclasse : </p>", unsafe_allow_html=True)
            st.image('streamlit_app/assets/synth_1.jpg', width=800)
            
            st.markdown("""
            Les performances de chaque algorithme sont évaluées en termes de précision classe_2, de rappel classe_2,
            de F1-score classe_2, de F1-score classe_3 et du score F1-macro global. Nous examinons également la possibilité
            de surapprentissage pour chaque modèle. Les meilleurs algorithmes sont les suivants : Random Forest
                """)
            
        with col5:
            #st.image('streamlit_app/assets/synth_2.jpg', caption="Synthèse des résultats en binaire", width=874)
        
            st.markdown("<p style='font-weight: bold; font-size: 20px; text-align: left;'>Synthèse des résultats en binaire : </p>", unsafe_allow_html=True)
            st.image('streamlit_app/assets/synth_2.jpg', width=800)
            
            st.markdown("""
            Les performances de chaque algorithme sont évaluées en termes de précision positive, de rappel positif, de
            F1-score négatif, de F1-score positif et du score F1-macro global. Nous examinons également la possibilité de
            surapprentissage pour chaque modèle. Les meilleurs algorithmes sont les suivants : Random Forest et Logistique
            régression.
                """)


#     st.markdown(
#         """
# Dans notre projet de prédiction de la gravité des accidents routiers, notre objectif est de prédire la variable
# cible 'grav', qui représente la gravité des blessures subies par les usagers accidentés. Ces usagers sont classés en
# quatre catégories : 1 - Indemne, 2 - Tué, 3 - Blessé, 4 - Blessé léger.
# Voici réparation de la variable grave dans notre dataset :
# Dans le cadre de notre étude, nous explorons deux approches de classification distinctes :
#         """
#     )
#     st.markdown("## Classification multiclasses")
    
#     st.markdown(
# """la classification multiclasse offre une perspective plus nuancée en classant
# les usagers accidentés en quatre catégories distinctes : "Indemne", "Tué", "Blessé", et "Blessé léger".
# Cette approche permet de saisir différentes nuances de gravité des blessures.""")
    
#     st.markdown(
# """Voici réparatition de la variable grave dans notre dataset :""")
    
#     X, y = load_data_from_csv_multi()
#     class_percentages = get_class_percentages(y)
#     st.table(class_percentages.assign(hack='').set_index('hack'))
    
#     st.markdown("#### Résultats de la classification multiclasse")
    
#     st.markdown("""nous comparons les performances des différents algorithmes de classification utilisés pour
# prédire la gravité des accidents dans le cas multiclass. Nous évaluons les modèles sur l'ensemble de test.""")
    
#     # st.image("streamlit_app/assets/resultat-multiclasse.png", caption='Résultats', use_column_width=True)
#     st.image("streamlit_app/assets/resultat-multiclasse.png", caption='Résultats', width=818)
    
#     st.markdown("""Les performances de chaque algorithme sont évaluées en termes de précision classe_2, de rappel classe_2,
# de F1-score classe_2, de F1-score classe_3 et du score F1-macro global. Nous examinons également la possibilité
# de surapprentissage pour chaque modèle. Les meilleurs algorithmes sont les suivants : Random Forest.""")
    
    
#     st.markdown( "## Classification Binaire")
    
#     st.markdown(
# """Cette approche simplifiée regroupe les usagers accidentés en deux catégories : 0 -"pas grave" et 1-
# "grave". Les avantages de cette approche résident dans sa simplicité, sa facilité d'interprétation et sa
# capacité à distinguer clairement les cas non graves des cas graves.""")
    
#     st.markdown(
# """Voici réparation de la variable grave dans notre dataset :""")
    
#     X, y = load_data_from_csv_binary()
#     class_percentages = get_class_percentages_binary(y)
#     st.table(class_percentages.assign(hack='').set_index('hack'))
    

#     st.markdown("""
#     Dans notre contexte, nous attachons une grande importance à minimiser les faux négatifs (FN). c'est-à-dire à
# éviter les erreurs où le modèle prédit que l'accident n'est pas grave alors qu'il l'est en réalité.""") 
    
#     # st.image("streamlit_app/assets/matrice-de-confusion FNTP.png", caption='Ouille', use_column_width=True)
#     st.image("streamlit_app/assets/matrice-de-confusion FNTP.png", caption='Matrice de confusion', width=585)
       
#     st.markdown("#### Résultats de la classification binaire")
    
#     st.markdown("""nous comparons les performances des différents algorithmes de classification utilisés pour
# prédire la gravité des accidents dans le cas multiclass. Nous évaluons les modèles sur l'ensemble de test.""")
    
#     # st.image("streamlit_app/assets/resultat-binaire.png", caption='Résultats', width=image_width)
#     st.image("streamlit_app/assets/resultat-binaire.png", caption='Résultats', width=763)

#     st.markdown("""Les performances de chaque algorithme sont évaluées en termes de précision positive, de rappel positif, de
# F1-score négatif, de F1-score positif et du score F1-macro global. Nous examinons également la possibilité de
# surapprentissage pour chaque modèle. Les meilleurs algorithmes sont les suivants : Random Forest et Logistique
# régression.""")

#     st.markdown("#### SHAP")
    
#     st.markdown("""Le SHAP global donne une vision d'ensemble de l'impact des caractéristiques sur le modèle. Il permet
# d'identifier quelles sont les caractéristiques qui ont, en moyenne, le plus d'impact sur les prédictions sur l'ensemble
# du jeu de données.
# Pour notre jeu de données le diagramme SHAP est le suivant :""")
    
#     # st.image("streamlit_app/assets/shap global binary.png", caption='Shap global', use_column_width=True)
#     st.image("streamlit_app/assets/shap global binary.png", caption='Shap global', width=767)

#     st.markdown("""À partir de l'analyse du diagramme SHAP, nous pouvons identifier les variables ayant le plus d'impact sur
# les prédictions du modèle. Les variables les plus impactantes sont celles relatives à la catégorie d'usager, l'obstacle
# mobile heurté, la localisation en agglomération ou non, la catégorie du véhicule, la présence d'équipement de
# sécurité, ainsi que l'âge du conducteur et de l'usager.
# Toutefois, il est à noter que des valeurs bleues et rouges sont présentes pour chacune de ces caractéristiques,
# ce qui reflète la complexité des relations dans les données.""")
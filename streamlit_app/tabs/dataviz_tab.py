import os
import streamlit as st
import pandas as pd
import numpy as np
from bokeh.io import output_notebook, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
# from bokeh.layouts import gridplot, layout
from bokeh.models.widgets import Panel, Tabs
from bokeh.io import curdoc
import pydeck as pdk
import joblib
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report

import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

import plotly.io as pio
pio.renderers.default = 'notebook'

title = "Dataviz"
sidebar_name = "Dataviz"

def part0():
    st.image("streamlit_app/assets/map.jpg", caption='Répartition des accidents par zone et gravité', width=1368)

def part1():

    st.image("streamlit_app/assets/covid.jpg", caption='Anomalie liée aux confinements du Covid ', width=1368)

def part2():    
    # st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    # st.markdown("## Présentation de quelques variables") 

    st.code(""" La variable agg - Localisation : 
                1 - Hors agglomération
                2 - En agglomération""")

    col1, col2 = st.columns([1,1])
    with col1:
        st.image("streamlit_app/assets/agg_1.jpg", caption='', width=666)
    with col2:
        st.image("streamlit_app/assets/agg_2.jpg", caption='', width=690)


def part3():
    
    st.code(""" La variable obs - Obstacle fixe heurté : 
                (-1) - Non renseigné                                                9 - Mobilier urbain
                0 - Sans objet                                                      10 - Parapet
                1 - Véhicule en stationnement                                       11 - Ilot, refuge, borne haute
                2 - Arbre                                                           12 - Bordure de trottoir
                3 - Glissière métallique                                            13 - Fossé, talus, paroi rocheuse
                4 - Glissière béton                                                 14 - Autre obstacle fixe sur chaussée
                5 - Autre glissière                                                 15 - Autre obstacle fixe sur trottoir ou accotement
                6 - Bâtiment, mur, pile de pont                                     16 - Sortie de chaussée sans obstacle
                7 - Support de signalisation verticale ou poste d'appel d'urgence   17 - Buse - tête d'aqueduc
                8 - Poteau""")

    st.image("streamlit_app/assets/obs.jpg", caption='', width=1070)

    st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)    


def part4():
    
    df_propre = pd.read_csv("data/dataset_18-21_usagers_propre.csv")

    feature_x = st.selectbox("Which feature on x?", df_propre.columns, index=3)
    feature_y = st.selectbox("Which feature on y?", df_propre.columns, index=2)
    # st.write(df_temp)
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


    st.write('Visualiser hist de variable', key="odddddn")
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


def connect_data_csv():
    """Connect to the data csv file"""
    my_path = "Exploratory Data Analysis/merged_data_2019_2021_for_streamlit.csv"
    # my_path = "C:/Users/dufou/OneDrive/Z-Python/Datascientest/Projet/FEV23_CDS_accidents/Exploratory Data Analysis/merged_data_2019_2021_for_streamlit.csv"
    df = pd.read_csv(my_path, sep=",", index_col=0)
    df['date'] = pd.to_datetime(df['date'])
    df['grav'] = df['grav'].replace([1, 4], 0).replace([2, 3], 1)
    print(df.info())
    return df

def filter_dataframe(df):
    # Filtrage par date
    min_date = df['date'].min().date()
    max_date = df['date'].max().date()
    start_date, end_date = st.date_input("Sélectionnez la plage de dates", [min_date, max_date])
    df = df[(df['date'].dt.date >= start_date) & (df['date'].dt.date <= end_date)]
    
    # Filtrage par 'mois'
    mois_choisis = st.multiselect("Sélectionnez un ou plusieurs mois:", sorted(df['mois'].unique()), default=sorted(df['mois'].unique()))
    df = df[df['mois'].isin(mois_choisis)]

    # Filtrage par 'age'
    ages_uniques = sorted(df['age_cond'].unique())
    ages_choisis = st.multiselect("Sélectionnez les tranches d'âge:", ages_uniques, default=ages_uniques)
    df = df[df['age_cond'].isin(ages_choisis)]

    # Filtrage par 'periode' avec boutons radio
    periodes = sorted(df['periode'].unique())
    periodes.insert(0, "Toutes les périodes")
    periode_choisie = st.radio("Sélectionnez une période:", periodes)
    if periode_choisie != "Toutes les périodes":
        df = df[df['periode'] == periode_choisie]

    # filtrage par gravité
    #grav_mapping = {"grave": 1, "léger": 0}
    #selected_label = st.radio("Sélectionnez la gravité:", list(grav_mapping.keys()))
    #selected_grav = grav_mapping[selected_label]
    # df = df[df['grav'] == selected_grav]
    # df.dropna(inplace=True)
    
# Calcul du nombre total de cas, des cas graves et légers
    total_cas = len(df)
    cas_graves = len(df[df['grav'] == 1])  # Remplacer '1' par la valeur appropriée pour les cas graves
    cas_legers = len(df[df['grav'] == 0])  # Remplacer '0' par la valeur appropriée pour les cas légers

    # Affichage des résultats
    st.write(f"Nombre total de cas après filtrage: {total_cas}, dont {cas_graves} cas graves et {cas_legers} cas légers")
    
    return df


def display_map_2(df):
    # Préparation des données
    map_df = df[['dep', 'dep_long', 'dep_lat', 'grav']]
    count_df = map_df.groupby(['dep', 'dep_long', 'dep_lat']).size().reset_index(name='total_count')
    grav_df = map_df[map_df['grav'] == 1].groupby(['dep', 'dep_long', 'dep_lat']).size().reset_index(name='grav_count')

    # Fusionner les DataFrames sur les colonnes 'dep', 'dep_long', 'dep_lat'
    map_df = pd.merge(count_df, grav_df, on=['dep', 'dep_long', 'dep_lat'], how='left')
    map_df['grav_count'] = map_df['grav_count'].fillna(0)

    # Calculer la part de la gravité
    map_df['grav_part'] = map_df['grav_count'] / map_df['total_count']

    # Visualisation
    # Plus la part est élevée, plus la couleur est proche du rouge foncé.
    cmap = plt.cm.YlOrRd

    # Normaliser la colonne 'proportion_grave'
    norm = plt.Normalize(vmin=map_df['grav_part'].min(), vmax=map_df['grav_part'].max())

    # Créer une nouvelle colonne pour la couleur
    map_df['color'] = map_df['grav_part'].apply(lambda x: [int(255 * c) for c in cmap(norm(x))[:3]] + [255])

    layer = pdk.Layer(
        "ScatterplotLayer",
        map_df,
        pickable=True,
        opacity=0.6,
        stroked=True,
        filled=True,
        radius_scale=4,
        radius_min_pixels=5,
        radius_max_pixels=50,
        line_width_min_pixels=1,
        get_position=["dep_long", "dep_lat"],
        get_radius="total_count*1.2",  # Ajuster selon la nécessité
        get_fill_color="color",
        get_line_color=[0, 0, 0],
    )


    # Configuration de la vue initiale de la carte
    view_state = pdk.ViewState(
        latitude=46.603354,
        longitude=1.888334,
        zoom=5,
        min_zoom=5,
        max_zoom=15,
        pitch=0,
        bearing=0
    )

    # Affichage de la carte avec Streamlit
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v10",
        initial_view_state=view_state,
        layers=[layer],
        height=1000
    ))


def afficher_tableau_2(df):
    # Grouper par département et gravité, et compter les incidents
    count_df = df.groupby(['dep', 'nom', 'grav']).size().reset_index(name='Nombre d\'accidents graves')

    # Calculer le total des accidents par département
    total_df = df.groupby(['dep', 'nom']).size().reset_index(name='Total accidents')

    # Fusionner les DataFrames pour calculer la part des accidents graves
    merged_df = pd.merge(count_df, total_df, on=['dep', 'nom'])

    # Filtrer pour les accidents graves (grav == 1) et calculer la part
    merged_df = merged_df[merged_df['grav'] == 1]
    merged_df['Part des accidents graves'] = merged_df['Nombre d\'accidents graves'] / merged_df['Total accidents']

    # Trier par 'Part des accidents graves' ou autre critère au choix
    merged_df = merged_df.sort_values(by='Total accidents', ascending=False)

    # Affichage du DataFrame dans Streamlit
    st.dataframe(merged_df[['dep', 'nom', 'Nombre d\'accidents graves', 'Total accidents', 'Part des accidents graves']], width=2000, height=800)



def ajuster_couleur(couleur, compte, compte_max):
    facteur = 1 - compte / compte_max
    couleur_ajustee = [
        int(couleur[0] * facteur),
        int(couleur[1] * facteur),
        int(couleur[2] * facteur),
        255  # Définir alpha à sa valeur maximale pour tous les points
    ]
    return couleur_ajustee

def display_map(df):

    map_df = df[['dep','dep_long', 'dep_lat', 'grav']]
    map_df = map_df.groupby(['dep','dep_long', 'dep_lat', 'grav']).size().reset_index(name='count')
    print(map_df.head())
    # grav_counts = map_df['grav'].value_counts()
    
    max_count = map_df['count'].max()
    color_map = {
    0: [0, 255, 0, 150],   # Rouge pour gravité 0
    1: [255, 0, 0, 150],   # Vert pour gravité 1
    }
    map_df['base_color'] = map_df['grav'].map(color_map)
    map_df['color'] = map_df.apply(lambda row: ajuster_couleur(row['base_color'], row['count'], max_count), axis=1)

    tooltip = {"text": "Numéro de département: {dep}"}
    
    layer = pdk.Layer(
        "ScatterplotLayer",
        map_df,
        pickable=True,
        opacity=0.6,
        stroked=True,
        filled=True,
        radius_scale=6,
        radius_min_pixels=10,
        radius_max_pixels=100,
        line_width_min_pixels=1,
        get_position=["dep_long", "dep_lat"],
        get_radius='count*2',
        get_fill_color="color",
        get_line_color=[0, 0, 0],
        tooltip=tooltip
    )

    view_state = pdk.ViewState(
        latitude=46.603354,
        longitude=1.888334,
        zoom=1,
        min_zoom=5,
        max_zoom=15,
        pitch=0,
        bearing=0
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v10",
        initial_view_state=view_state,
        layers=[layer]
    ))


def afficher_tableau(df):
    print(df.head())
    map_df = df[['dep','nom', 'grav']]
    map_df = map_df.groupby(['dep','nom', 'grav']).size().reset_index(name='Nombre d\'accidents')
    map_df = map_df.sort_values(by='Nombre d\'accidents', ascending=False)
    st.dataframe(map_df, width=2000, height=800)
    
def create_chart(df):
    
    #df['date'] = pd.to_datetime(df['date']) 
    values = df['date'].value_counts().sort_index()
    data = pd.DataFrame({'date': values.index, 'values': values})

    panels = []

    for year in data['date'].dt.year.unique():
    
        # Filtrage des données pour l'année en cours
        data_year = data[data['date'].dt.year == year]
        data_year = data_year.drop(columns=['date'])
        source = ColumnDataSource(data_year)
    
        p = figure(title=f"Nombre d'accident par jour en {year}",
               x_axis_label="Date",
               y_axis_label="Nombre d'accidents",
               x_axis_type='datetime',
               width=900,
               height=400)
    
        p.line(x="date",
               y="values",
            source=source,
            line_width=2)
    
        circles = p.circle(x="date",
                       y="values",
                       source=source,
                       size=8,
                       fill_color="white",
                       line_color="blue")
    
        hover = HoverTool(tooltips=[("Date", "@date{%F}"),
                                ("Nombre d'accidents", "@values")],
                      formatters={"@date": "datetime"},
                      mode='vline')
    
        p.add_tools(hover)
        curdoc().theme = 'night_sky'
    
    # Création d'un Panel pour cette année et ajout à la liste des panels
        panel = Panel(child=p, title=str(year))
        panels.append(panel)

    # Création des onglets à partir des panels
    tabs = Tabs(tabs=panels)

    #output_notebook()
    # show(tabs)
    return tabs

    
def plot_agg_graph(df):
    
    # Group by 'agg' and 'grav' and count the number of accidents
    grouped = df.groupby(['agg', 'grav']).size().unstack()

    # Create a grouped bar plot with new colors
    colors = ["#27ae60", "#7b241c"]  # Green for léger, Bordeaux for grave
    grouped.plot(kind='bar', figsize=(8,4), color=colors, edgecolor='black', width=0.7)

    plt.title("Nombre d'accidents hors ou en agglomération et gravité", fontsize=18, fontweight='bold')
    plt.xlabel("Localisation", fontsize=15)
    plt.ylabel("Nombre d'accidents", fontsize=15)
    labels = ['hors-agglomération', 'agglomération']
    plt.xticks(ticks=range(len(labels)), labels=labels, rotation=0, fontsize=12)
    plt.legend(title="Gravité", labels=["léger", "grave"])
    plt.grid(axis='y', alpha=0.75)
    
    plt.tight_layout()
    plt.show()


def plot_col_graph(df):
    # Group by 'agg' and 'grav' and count the number of accidents
    grouped = df.groupby(['col', 'grav']).size().unstack()

    # Create a grouped bar plot with new colors
    colors = ["#27ae60", "#7b241c"]  # Green for léger, Bordeaux for grave
    grouped.plot(kind='bar', figsize=(8, 5), color=colors, edgecolor='black', width=0.7)

    plt.title("Nombre d'accidents par type de collision et gravité", fontsize=18, fontweight='bold')
    plt.xlabel("", fontsize=15)
    plt.ylabel("Nombre d'accidents", fontsize=15)
    labels = ['Sans collision', 'Autres collisions', "Deux véhicules frontales", "Autres coll. entre véhicules"]
    plt.xticks(ticks=range(len(labels)), labels=labels, rotation=25, fontsize=12)
    plt.legend(title="Gravité", labels=["léger", "grave"])
    plt.grid(axis='y', alpha=0.75)
    
    plt.tight_layout()
    plt.show()



# *********************************************************************************************************************************************************** #
def run(image_width):

    # st.title(title)

    sections = ["Carte interactive des accidents", "Evolution des accidents", "Présentation de la variable agg", "Présentation de la variable obs"]

    # Navigation avec des boutons radio    
    # st.markdown("## Sommaire")
    selected_section = st.radio("", sections)

    # Affiche le contenu en fonction de la section choisie
    if selected_section == "Carte interactive des accidents":
        st.header("Carte interactive des accidents")
        st.markdown("---")
        

        st.markdown(
        """
    Sur cette carte, vous pouvez visualiser la distribution géographique des accidents à travers différents départements de France.
    Chaque point sur la carte représente un département, et la taille et la couleur du point indiquent le nombre et la gravité des accidents.
        """)

        df = connect_data_csv()
        
        st.markdown("<div style='height:50px;'></div>", unsafe_allow_html=True)
    
        df = filter_dataframe(df)
    
        display_map_2(df)
    
        with st.expander("Afficher/Masquer les données brutes"):
            afficher_tableau_2(df)
    
       
        st.markdown("<div style='height:50px;'></div>", unsafe_allow_html=True)
    
        st.markdown(
        """
    Ce graphique illustre la tendance et la distribution des accidents au fil du temps.
    Chaque ligne représente une année, et vous pouvez naviguer entre les différentes années à l'aide des onglets.
        """
    )
    
        chart = create_chart(df)
        st.bokeh_chart(chart)

        st.markdown("<div style='height:50px;'></div>", unsafe_allow_html=True)






    elif selected_section == "Evolution des accidents":
        st.header("Evolution des accidents")
        st.markdown("---")
        part1()

    elif selected_section == "Présentation de la variable agg":
        st.header("La variable agg")
        st.markdown("---")
        part2()

    elif selected_section == "Présentation de la variable obs":
        st.header("La variable obs")
        st.markdown("---")
        part3()



    

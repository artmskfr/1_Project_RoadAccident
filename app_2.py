from collections import OrderedDict

import streamlit as st

# TODO : change TITLE, TEAM_MEMBERS and PROMOTION values in config.py.
from streamlit_app import config

# TODO : you can (and should) rename and add tabs in the ./tabs folder, and import them here.
from streamlit_app.tabs import contexte_tab, presentation_tab, dataviz_tab, preprocessing_tab, modelisation_tab, demo_tab, impact_tab, optimisation_tab, conclusion_tab, perspectives_tab

st.set_page_config(
    page_title=config.TITLE,
    page_icon="https://datascientest.com/wp-content/uploads/2020/03/cropped-favicon-datascientest-1-32x32.png",
    layout="wide"
)

with open("streamlit_app/style_white.css", "r") as f:
    style = f.read()

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)


# TODO: add new and/or renamed tab in this ordered dict by
# passing the name in the sidebar as key and the imported tab
# as value as follow :
TABS = OrderedDict(
    [
        (contexte_tab.sidebar_name, contexte_tab),
        (presentation_tab.sidebar_name, presentation_tab),
        (dataviz_tab.sidebar_name, dataviz_tab),
        (preprocessing_tab.sidebar_name, preprocessing_tab),
        (modelisation_tab.sidebar_name, modelisation_tab),
        (demo_tab.sidebar_name, demo_tab),
        (impact_tab.sidebar_name, impact_tab),
        # (optimisation_tab.sidebar_name, optimisation_tab),
        (conclusion_tab.sidebar_name, conclusion_tab),
        (perspectives_tab.sidebar_name, perspectives_tab)
    ]
)

def run():
    # Sidebar CSS selector
    import os
    all_files = os.listdir("streamlit_app/")
    css_files = [f for f in all_files if f.endswith('.css')]
    selected_css = st.sidebar.selectbox("Selection du thème", css_files)
    with open(f"streamlit_app/{selected_css}", "r") as f:
        style = f.read()
        st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)
    #st.sidebar.image(
    #    "https://dst-studio-template.s3.eu-west-3.amazonaws.com/logo-datascientest.png",
    #    width=200,
    #)
    
    image_width = st.sidebar.slider("Largeur de l'image", min_value=50, max_value=1000, value=500, step=50)
    # st.sidebar.markdown("--------")
    st.sidebar.markdown("## **Accident de la route**")
    tab_name = st.sidebar.radio("", list(TABS.keys()), 0)
    # st.sidebar.markdown("--------")
    st.sidebar.markdown(f"## {config.PROMOTION}")

    st.sidebar.markdown("### Team members:")
    for member in config.TEAM_MEMBERS:
        st.sidebar.markdown(member.sidebar_markdown(), unsafe_allow_html=True)

    tab = TABS[tab_name]

    tab.run(image_width)


if __name__ == "__main__":

    run()

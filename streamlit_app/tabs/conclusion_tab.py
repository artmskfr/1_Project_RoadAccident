import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


title = "Conclusions"
sidebar_name = "Conclusions"


def run(image_width):

    st.title(title)
    st.markdown("---")
    st.image('streamlit_app/assets/conclu.jpg', caption = "", width=1362)



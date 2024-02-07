import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


title = "Perspectives"
sidebar_name = "..."


def run(image_width):

    st.title(title)
    st.markdown("---")
    st.image('streamlit_app/assets/next.jpg', caption = "", width=1023)



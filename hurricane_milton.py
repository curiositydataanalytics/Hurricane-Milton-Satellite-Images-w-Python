# Data manipulation
import numpy as np
import datetime as dt
import pandas as pd
import geopandas as gpd

# Database and file handling
import os

# Data visualization
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import graphviz
import pydeck as pdk

path_cda = '\\CuriosityDataAnalytics'
path_wd = path_cda + '\\wd'
path_data = path_wd + '\\data'

# App config
#----------------------------------------------------------------------------------------------------------------------------------#
# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)



# App title
st.title("Hurricane Milton Satellite Imagery")
st.divider()

with st.sidebar:
    st.image(path_cda + '\\logo.png')

#
#

cols = st.columns(4)

cols[0].header('GeoColor')
with cols[0].expander(''):
    st.image(path_data + '\\geocolor.gif')

cols[1].header('Sandwich RGB')
with cols[1].expander(''):
    st.image(path_data + '\\sandwich.gif')

cols[2].header('Day Night Cloud Micro Combo RGB')
with cols[2].expander(''):
    st.image(path_data + '\\DayNightCloudMicroCombo.gif')

cols[3].header('Airmass RGB')
with cols[3].expander(''):
    st.image(path_data + '\\airmass.gif')
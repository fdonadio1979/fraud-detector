import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk


@st.cache
def load_data_time(nrows):
    data_t = pd.read_csv("raw-data1.csv", nrows=nrows, index_col = "Hours")
    return (data_t)

@st.cache
def load_data_distance(nrows):
    data_d = pd.read_csv("raw-data1.csv", nrows=nrows, index_col = "Distance")
    return (data_d)

# nrows = st.number_input('Insert a number', max_value=10000, min_value=0, value=100)

last_value = df1.index[-1].round(decimals=1)
sel_value = st.slider('track', max_value=last_value, min_value=0, value=last_value)
nrows = sel_value * 1650 / last_value


df1 = load_data_time(nrows)
if st.checkbox('Time/Distance Index'):
    df1 = load_data_distance(nrows)



midpoint = (np.average(df1["Lat"]), np.average(df1["Lon"]))

st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state={
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11.7,
        "pitch": 60,
    },
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=df1,
            get_position=["Lon", "Lat"],
            radius=100,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
    ],
))
# st.altair_chart(alt.Chart(df1))

# st.map(df1,11)
st.area_chart(df1['Speed'])


df2 = df1[['VolTotal', 'Vol1', 'Vol2', 'Vol3', 'Vol4', 'Vol5', 'Vol6']]
columns = st.multiselect(
    label='What tank do you want to display?', options=df2.columns)
    
st.area_chart(df2[columns])

if st.checkbox('Show dataframe'):
    st.write(df2)

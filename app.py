import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk



@st.cache
def load_data_time(nrows, skiprows):
    data_t = pd.read_csv("raw-data1.csv", nrows = nrows, index_col = "Hours", skiprows=[i for i in range(1,skiprows)])
    return (data_t)

@st.cache
def load_data_distance(nrows, skiprows):
    data_d = pd.read_csv("raw-data1.csv", nrows = nrows, index_col = "Distance", skiprows=[i for i in range(1,skiprows)])
    return (data_d)

# nrows = st.number_input('Insert a number', max_value=10000, min_value=0, value=100)



if st.sidebar.checkbox('Time/Distance Index'):
    df1 = load_data_distance(1650, 1)
    max_value = df1.index[-1].round(decimals=1)
    sel_value = st.sidebar.slider('Distance [Km]', 0.1, max_value, (0.1, max_value))
    nrows = int (sel_value[1] * 1650 / max_value)
    skiprows = int (sel_value[0] * 1650 / max_value)
    df1 = load_data_distance(nrows-skiprows, skiprows)
else:
    df1 = load_data_time(1650, 1)
    max_value = df1.index[-1].round(decimals=1)
    sel_value = st.sidebar.slider('Time [Hours]', 0.1, max_value, (0.1, max_value))
    nrows = int (sel_value[1] * 1650 / max_value)
    skiprows = int (sel_value[0] * 1650 / max_value)
    df1 = load_data_time(nrows-skiprows, skiprows)



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

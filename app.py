import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

@st.cache
def load_data_time(nrows):
    data_t = pd.read_csv("raw-data1.csv", nrows=nrows, index_col = "Date/Time")
    return (data_t)

@st.cache
def load_data_distance(nrows):
    data_d = pd.read_csv("raw-data1.csv", nrows=nrows, index_col = "Distance")
    return (data_d)

# nrows = st.number_input('Insert a number', max_value=1652, min_value=0, value=100)
nrows = st.slider('track', max_value=1652, min_value=0, value=500)

df1 = load_data_time(nrows)
if st.checkbox('Time/Distance Index'):
    df1 = load_data_distance(nrows)

midpoint = (np.average(df1["Lat"]), np.average(df1["Lon"]))

st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state={
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=df1,
            get_position=["lon", "lat"],
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
st.area_chart(df1['VolTotal'])



# @st.cache
# def fetch_data(SW):
    # data = pd.read_csv("raw-data.csv",index_col = "TIME")
    # if Km:
        # data = pd.read_csv("raw-data.csv",index_col = "DISTANCE")
    # return (data)
    
# df1 = fetch_data()
# if st.checkbox('Show dataframe'):
    # st.write(df1)
# # st.map(df1)
# st.area_chart(df1['HEIGHT'])

# df2 = pd.read_csv("raw-data.csv")
# st.area_chart(df2)

# chart_data = pd.DataFrame(
    # np.random.randn(20, 3),
    # columns=['a', 'b', 'c'])

# st.area_chart(chart_data)
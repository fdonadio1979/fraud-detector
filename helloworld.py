import streamlit as st
import pandas as pd
import numpy as np

@st.cache
def load_data_time(nrows):
    data_t = pd.read_csv("raw-data.csv", nrows=nrows, index_col = "TIME")
    return (data_t)

@st.cache
def load_data_distance(nrows):
    data_d = pd.read_csv("raw-data.csv", nrows=nrows, index_col = "DISTANCE")
    return (data_d)

nrows = st.number_input('Insert a number', max_value=10000, min_value=0, value=100)

df1 = load_data_time(nrows)
if st.checkbox('Time/Distance Index'):
    df1 = load_data_distance(nrows)

st.map(df1)    
st.area_chart(df1['HEIGHT'])


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
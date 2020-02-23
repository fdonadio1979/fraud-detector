import streamlit as st
import pandas as pd
import numpy as np

Km = st.checkbox('Km')
@st.cache
def fetch_data():
    data = pd.read_csv("raw-data.csv",index_col = "TIME")
    if Km:
        data = pd.read_csv("raw-data.csv",index_col = "DISTANCE")
    return (data)
    
df1 = fetch_data()
if st.checkbox('Show dataframe'):
    st.write(df1)
# st.map(df1)
st.area_chart(df1['HEIGHT'])

# df2 = pd.read_csv("raw-data.csv")
# st.area_chart(df2)

# chart_data = pd.DataFrame(
    # np.random.randn(20, 3),
    # columns=['a', 'b', 'c'])

# st.area_chart(chart_data)
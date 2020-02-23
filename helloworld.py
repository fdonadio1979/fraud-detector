import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("raw-data.csv")
if st.checkbox('Show dataframe'):
    st.write(df)
st.map(df)

st.area_chart(df)

# chart_data = pd.DataFrame(
    # np.random.randn(20, 3),
    # columns=['a', 'b', 'c'])

# st.area_chart(chart_data)
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("29148163867.csv")
if st.checkbox('Show dataframe'):
    st.write(df)
st.map(df)

st.area_chart(df)
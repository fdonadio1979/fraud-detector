import streamlit as st
import pandas as pd
import numpy as np

df1 = pd.read_csv("raw-data.csv")
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
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("29148163867.csv", columns=['INDEX', 'RCR', 'DATE', 'TIME', 'VALID', 'latitude', 'N/S', 'longitude', 'E/W', 'HEIGHT', 'SPEED', 'HEADING', 'DSTA', 'DAGE', 'PDOP', 'HDOP', 'VDOP', 'NSAT (USED/VIEW)', 'SAT INFO (SID-ELE-AZI-SNR)', 'DISTANCE'])
if st.checkbox('Show dataframe'):
    st.write(df)
st.map(df)
st.area_chart(df[TIME],df[HEIGHT])

# chart_data = pd.DataFrame(
    # np.random.randn(20, 3),
    # columns=['a', 'b', 'c'])

# st.area_chart(chart_data)
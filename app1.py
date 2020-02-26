import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk


# @st.cache
def load_data(filename):
    data = pd.read_csv(filename)
    return (data)

csv_file = 'raw-data1.csv'
df = load_data(csv_file)

supply_file = 'supplies1.csv'
supplies = load_data(supply_file)
supplies.set_index('Tank', inplace=True)


max_index = df.index[-1]
max_distance = df['Distance'].iloc[-1].round(decimals=1)
max_time = df['Hours'].iloc[-1].round(decimals=1)




index_type = st.sidebar.radio(
    "Select index type",
    ('Km', 'Hs'))

if index_type == 'Hs':
    max_value = max_time
    label = "Time [Hs]"
else:
    max_value = max_distance
    label = "Distance [Km]"

sel_value = st.sidebar.slider(label, 0.0, max_value, (0.0, max_value))

from_row = int (sel_value[0] * max_index / max_value)
to_row = int (sel_value[1] * max_index / max_value)

df5 = df.loc[from_row:to_row,'Lat':'Lon']
midpoint = (np.average(df["Lat"]), np.average(df["Lon"]))



tank = st.sidebar.radio(
    "Select tank",
    ('Total', 'Tank1', 'Tank2', 'Tank3', 'Tank4', 'Tank5', 'Tank6'))

if tank == 'Total':
	max_dif = max(df['DifVolTotal'])
	label_tank = "DifVolTotal"

max_diff = st.sidebar.slider(label_tank, 0.0, max_dif,5.0)


if tank == 'Total':
	df1 = supplies.loc['Total':'Total','Loading Date':'Elapsed Time']
	df2 = supplies.loc['Total':'Total','Loading Volume (@15C)':'Volume Diff']
	df3 = supplies.loc['Total':'Total','Origin':'Travelled Distance']
	df4 = supplies.loc['Total':'Total','Unit':'Customer']
	if index_type == 'Hs':
		df6 = df.loc[from_row:to_row,['VolTotal','Hours']]
		df7 = df.loc[from_row:to_row,['DifVolTotal','Hours']]
	else:
		df6 = df.loc[from_row:to_row,['VolTotal','Distance']]
		df7 = df.loc[from_row:to_row,['DifVolTotal','Distance']]
	df7 = df7[df7['DifVolTotal'] < max_diff]
	# df6 = df6[df6['VolTotal'].isin([sel_vol[1]:sel_vol[0]])])
	# df6 = df6[df6['VolTotal'].between(sel_vol[0], sel_vol[1])]
elif tank == 'Tank1':
	df1 = supplies.loc['Tank1':'Tank1','Loading Date':'Elapsed Time']
	df2 = supplies.loc['Tank1':'Tank1','Loading Volume (@15C)':'Volume Diff']
	df3 = supplies.loc['Tank1':'Tank1','Origin':'Travelled Distance']
	df4 = supplies.loc['Tank1':'Tank1','Unit':'Customer']
	if index_type == 'Hs':
		df6 = df.loc[from_row:to_row,['Vol1','Hours']]
		df7 = df.loc[from_row:to_row,['DifVol1','Hours']]
	else:
		df6 = df.loc[from_row:to_row,['Vol1','Distance']]
		df7 = df.loc[from_row:to_row,['DifVol1','Distance']]
	df7 = df7[df7.DifVolTotal < 5.0]
elif tank == 'Tank2':
	df1 = supplies.loc['Tank2':'Tank2','Loading Date':'Elapsed Time']
	df2 = supplies.loc['Tank2':'Tank2','Loading Volume (@15C)':'Volume Diff']
	df3 = supplies.loc['Tank2':'Tank2','Origin':'Travelled Distance']
	df4 = supplies.loc['Tank2':'Tank2','Unit':'Customer']
	if index_type == 'Hs':
		df6 = df.loc[from_row:to_row,['Vol2','Hours']]
		df7 = df.loc[from_row:to_row,['DifVol2','Hours']]
	else:
		df6 = df.loc[from_row:to_row,['Vol2','Distance']]
		df7 = df.loc[from_row:to_row,['DifVol2','Distance']]
elif tank == 'Tank3':
	df1 = supplies.loc['Tank3':'Tank3','Loading Date':'Elapsed Time']
	df2 = supplies.loc['Tank3':'Tank3','Loading Volume (@15C)':'Volume Diff']
	df3 = supplies.loc['Tank3':'Tank3','Origin':'Travelled Distance']
	df4 = supplies.loc['Tank3':'Tank3','Unit':'Customer']
	if index_type == 'Hs':
		df6 = df.loc[from_row:to_row,['Vol3','Hours']]
		df7 = df.loc[from_row:to_row,['DifVol3','Hours']]
	else:
		df6 = df.loc[from_row:to_row,['Vol3','Distance']]
		df7 = df.loc[from_row:to_row,['DifVol3','Distance']]
elif tank == 'Tank4':
	df1 = supplies.loc['Tank4':'Tank4','Loading Date':'Elapsed Time']
	df2 = supplies.loc['Tank4':'Tank4','Loading Volume (@15C)':'Volume Diff']
	df3 = supplies.loc['Tank4':'Tank4','Origin':'Travelled Distance']
	df4 = supplies.loc['Tank4':'Tank4','Unit':'Customer']
	if index_type == 'Hs':
		df6 = df.loc[from_row:to_row,['Vol4','Hours']]
		df7 = df.loc[from_row:to_row,['DifVol4','Hours']]
	else:
		df6 = df.loc[from_row:to_row,['Vol4','Distance']]
		df7 = df.loc[from_row:to_row,['DifVol4','Distance']]
elif tank == 'Tank5':
	df1 = supplies.loc['Tank5':'Tank5','Loading Date':'Elapsed Time']
	df2 = supplies.loc['Tank5':'Tank5','Loading Volume (@15C)':'Volume Diff']
	df3 = supplies.loc['Tank5':'Tank5','Origin':'Travelled Distance']
	df4 = supplies.loc['Tank5':'Tank5','Unit':'Customer']
	if index_type == 'Hs':
		df6 = df.loc[from_row:to_row,['Vol5','Hours']]
		df7 = df.loc[from_row:to_row,['DifVol5','Hours']]
	else:
		df6 = df.loc[from_row:to_row,['Vol5','Distance']]
		df7 = df.loc[from_row:to_row,['DifVol5','Distance']]
else:
	df1 = supplies.loc['Tank6':'Tank6','Loading Date':'Elapsed Time']
	df2 = supplies.loc['Tank6':'Tank6','Loading Volume (@15C)':'Volume Diff']
	df3 = supplies.loc['Tank6':'Tank6','Origin':'Travelled Distance']
	df4 = supplies.loc['Tank6':'Tank6','Unit':'Customer']
	if index_type == 'Hs':
		df6 = df.loc[from_row:to_row,['Vol6','Hours']]
		df7 = df.loc[from_row:to_row,['DifVol6','Hours']]
	else:
		df6 = df.loc[from_row:to_row,['Vol6','Distance']]
		df7 = df.loc[from_row:to_row,['DifVol6','Distance']]

# st.write(supplies)
# st.write(df)
# st.write(max_index)
# st.write(max_distance)
# st.write(max_time)
# st.write(sel_value)
# st.write(from_row)
# st.write(to_row)
# st.write(label)

st.write(df2)
st.write(df1)
st.write(df3)
st.write(df4)





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
            data=df5,
            get_position=["Lon", "Lat"],
            radius=100,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
    ],
))


if index_type == 'Hs':
	df6.set_index('Hours', inplace=True)
	df7.set_index('Hours', inplace=True)
else:
	df6.set_index('Distance', inplace=True)
	df7.set_index('Distance', inplace=True)

# st.write(df6)


st.area_chart(df6, use_container_width=True)

# st.write(df7)

st.area_chart(df7, use_container_width=True)

# st.write(supplies[['Loading Date','Unloading Date','Elapsed Time']].head(1))
# st.write(supplies.loc[0,['Loading Date','Unloading Date','Elapsed Time']])
# @st.cache
# def load_data_time(nrows, skiprows):
    # data_t = pd.read_csv("raw-data1.csv", nrows = nrows, index_col = "Hours", skiprows=[i for i in range(1,skiprows)])
    # return (data_t)

# @st.cache
# def load_data_distance(nrows, skiprows):
    # data_d = pd.read_csv("raw-data1.csv", nrows = nrows, index_col = "Distance", skiprows=[i for i in range(1,skiprows)])
    # return (data_d)

# # nrows = st.number_input('Insert a number', max_value=10000, min_value=0, value=100)



# if st.sidebar.checkbox('Km/Hours'):
    # df1 = load_data_distance(1650, 1)
    # max_value = df1.index[-1].round(decimals=1)
    # sel_value = st.sidebar.slider('Distance [Km]', 0.1, max_value, (0.1, max_value))
    # nrows = int (sel_value[1] * 1650 / max_value)
    # skiprows = int (sel_value[0] * 1650 / max_value)
    # df1 = load_data_distance(nrows-skiprows+1, skiprows)
# else:
    # df1 = load_data_time(1650, 1)
    # max_value = df1.index[-1].round(decimals=1)
    # sel_value = st.sidebar.slider('Time [Hours]', 0.1, max_value, (0.1, max_value))
    # nrows = int (sel_value[1] * 1650 / max_value)
    # skiprows = int (sel_value[0] * 1650 / max_value)
    # df1 = load_data_time(nrows-skiprows+1, skiprows)



# midpoint = (np.average(df1["Lat"]), np.average(df1["Lon"]))

# st.write(pdk.Deck(
    # map_style="mapbox://styles/mapbox/light-v9",
    # initial_view_state={
        # "latitude": midpoint[0],
        # "longitude": midpoint[1],
        # "zoom": 11.7,
        # "pitch": 60,
    # },
    # layers=[
        # pdk.Layer(
            # "HexagonLayer",
            # data=df1,
            # get_position=["Lon", "Lat"],
            # radius=100,
            # elevation_scale=4,
            # elevation_range=[0, 1000],
            # pickable=True,
            # extruded=True,
        # ),
    # ],
# ))

# st.area_chart(df1['Speed'])


# df2 = df1[['VolTotal', 'Vol1', 'Vol2', 'Vol3', 'Vol4', 'Vol5', 'Vol6']]
# columns1 = st.sidebar.multiselect(
    # label='What tank do you want to display?', options=df2.columns)
    
# st.area_chart(df2[columns1])

# df3 = df1[['DifVolTotal', 'DifVol1', 'DifVol2', 'DifVol3', 'DifVol4', 'DifVol5', 'DifVol6']]
# columns2 = st.sidebar.multiselect(
    # label='What tank do you want to display?', options=df3.columns)
    
# st.area_chart(df3[columns2])

# if st.sidebar.checkbox('Show dataframe'):
    # st.write(df3)
    
    

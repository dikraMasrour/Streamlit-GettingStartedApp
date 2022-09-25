import streamlit as st
import pandas as pd
import numpy as np


st.title('Uber pickups in NYC')

DATECOL = 'date/time'
DATAURL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATAURL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATECOL] = pd.to_datetime(data[DATECOL])
    return data 

# load data
data_load_state = st.text('Loading data ...')
data = load_data(10000)
data_load_state.text('Loading data ... done! (using cache)')

# toggle to show raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# histogram of pickups per hour
st.subheader('Number of pickups per hour')
hist_values = np.histogram(data[DATECOL].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# slider to filter data per time
hour_to_filter = st.slider('hour', 0, 23, 17) # min 0h, max 23h, default 17h
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
filtered_data = data[data[DATECOL].dt.hour == hour_to_filter]
st.map(filtered_data)
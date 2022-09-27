from random import random
from streamlit_ace import st_ace
import streamlit as st
import pandas as pd
import numpy as np


st.title('Final demo')

DATECOL = 'date/time'
DATAURL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'


# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATAURL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATECOL] = pd.to_datetime(data[DATECOL])
#     return data 

# load data
# data_load_state = st.text('Loading data ...')
# data = load_data(10000)
# data_load_state.text('Loading data ... done! (using cache)')

# # toggle to show raw data
# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# # histogram of pickups per hour
# st.subheader('Number of pickups per hour')
# hist_values = np.histogram(data[DATECOL].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# slider to filter data per time
# hour_to_filter = st.slider('hour', 0, 23, 17) # min 0h, max 23h, default 17h
# st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# filtered_data = data[data[DATECOL].dt.hour == hour_to_filter]
# st.map(filtered_data)


# def add_code_cell():
#     if 'codeCells' not in st.session_state:
#         st.session_state.codeCells = []
#     st.session_state.codeCells.append(st.text_input(label=f'code {random()}'))


# st.session_state.addButton = st.button('add code cell', on_click=add_code_cell)

# st.write(st.session_state.addButton)

# if st.session_state.addButton:
#     # add_code_cell()
#     st.write(st.session_state.codeCells)




if 'codeCells' not in st.session_state:
    st.session_state.codeCells = {}
    print('TYPEEEE', type(st.session_state.codeCells))


st.session_state.addButton = st.button('add code cell')


dict_len = len(st.session_state.codeCells)

if st.session_state.addButton:
    st.session_state.codeCells[dict_len] = 'write code'


for codecell in st.session_state.codeCells.copy():
    
    with st.container() as c: 
        coll, colr = st.columns([4,2])
        with coll:
            code =  st_ace(placeholder=codecell, language='python', height=80, auto_update=True)
        
        st.session_state.codeCells[codecell] = str(code)

        with colr:
            st.write(st.session_state.codeCells[codecell])
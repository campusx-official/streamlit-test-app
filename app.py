import pandas as pd
import streamlit as st
import json
import time

st.set_page_config(layout='wide')

startup = pd.read_csv('startup_funding.csv')

st.title('Streamlit Demo')

choice = st.sidebar.selectbox('Select',['Overall','Startup','Investor'])

if choice == 'Startup':
    selected_startup = st.sidebar.selectbox('Select Startup',['ola','uber'])
    btn1 = st.sidebar.button('View Details')
    if btn1:
        st.write('Hello')




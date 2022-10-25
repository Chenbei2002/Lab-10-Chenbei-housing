import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

st.title('California Housing data(1990) By Bei Chen')
df = pd.read_csv('housing.csv')

# create a price filter
price_filter = st.slider('Median House Price', 0.0, 500001.0, 200000.0)  # min, max, default

st.subheader('See more filters in the sidebar:')

# create a multi select--location
location_filter = st.sidebar.multiselect(
     'Chose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a income level
income_filter = st.sidebar.radio(
    "Chose income level",
    ('Low', 'Median', 'High'))
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Median':
    df = df[(df.median_income >2.5) & (df.median_income<4.5)]
elif income_filter == 'High':
    df = df[df.median_income >4.5]

# filter by price
df = df[df.median_house_value >= price_filter]

# filter by location
df = df[df.ocean_proximity.isin(location_filter)]

# show on map
st.map(df)

#create a hist
st.subheader('Histogram of the median house value')
fig, ax = plt.subplots(figsize=(15, 10))
df.median_house_value.hist(bins=30)
st.pyplot(fig)

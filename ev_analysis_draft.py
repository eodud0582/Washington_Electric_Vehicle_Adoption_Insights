# ev_analysis.py
import pickle
import numpy as np
import pandas as pd

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

import streamlit as st

# load data
@st.cache_data
def load_data():
    with open('MSU/Fall_2024/CMSE_830/midterm/data/ev_elec.pickle', 'rb') as f:
        ev_elec = pickle.load(f)
    with open('MSU/Fall_2024/CMSE_830/midterm/data/charger.pickle', 'rb') as f:
        charger = pickle.load(f)
    # ev_elec = pd.read_csv('data/ev_elec.csv')
    # ev_charger = pd.read_csv('data/alt_fuel_stations.csv')
    return ev_elec, charger

ev_elec, charger = load_data()

# Title
st.title("Washington State EV Adoption")

# Introduction
st.markdown("""
# Electric Vehicle (EV) Registration Dashboard

**Target Audience:** Washington State Government and Automotive Industry Stakeholders

This dashboard shows the current status of electric vehicle (EV) registrations in Washington State. 
It explores the relationship between EV adoption, political trends, and infrastructure developments, including charging stations.
""")

# Interactive/filtering option test
districts = ev_elec['legislative_district'].unique()
selected_district = st.sidebar.multiselect("Select Legislative District(s):", districts)

if selected_district:
    ev_elec = ev_elec[ev_elec['legislative_district'].isin(selected_district)]
    charger = charger[charger['legislative_district_upper'].isin(selected_district)]

# Basic statistics of the main EV dataset
st.markdown("## Basic EV Statistics")

st.write(ev_elec.describe())

# Washington state ev status compared to other states
st.markdown("""
Washington state ev status compared to other states
""")

# EV Population by Political Party
st.header("EV Population by Political Party")

st.markdown("""
2022 senate election result in washington state..

blah

Democratic party leaning

blah
""")

party_colors = {'Democratic': '#3333FF', 'Republican': '#FF3333'}
fig = px.histogram(ev_elec, x="legislative_district", color="party_won_ld", 
                   color_discrete_map=party_colors,
                   title="EV Population by Political Party",
                   labels={'party_won_ld': 'Party Won'})

st.plotly_chart(fig)

# EV and Charging Station Comparison
st.header("EV and Charging Station Comparison")

fig, axs = plt.subplots(2, figsize=(10, 8))

# Plot 1: EV by district
sns.countplot(data=ev_elec, x='legislative_district', hue='party_won_ld', palette=party_colors, ax=axs[0])
axs[0].set_title('EV Population by Legislative District')
axs[0].set_xlabel('Legislative District')
axs[0].set_ylabel('EV Population')

# Plot 2: Charger by district
sns.countplot(data=charger, x='legislative_district_upper', order=ev_elec['legislative_district'].value_counts().index, ax=axs[1])
axs[1].set_title('Charging Station Count by Legislative District')
axs[1].set_xlabel('Legislative District')
axs[1].set_ylabel('Charger Count')

st.pyplot(fig)

# Charger to EV Ratio
st.header("Charger to EV Ratio")

charger_count = charger['legislative_district_upper'].value_counts()
ev_count = ev_elec['legislative_district'].value_counts()
ratio = charger_count / ev_count

fig = px.bar(x=ratio.index, y=ratio.values, title="Charger to EV Ratio by District")
st.plotly_chart(fig)

# Environmental Impact of EV Adoption (optional)
st.header("Environmental Impact of EV Adoption")

st.markdown("""
We can explore whether increased EV adoption ... across Washington State.

blah blah
""")

# streamlit run MSU/Fall_2024/CMSE_830/midterm/ev_analysis.py

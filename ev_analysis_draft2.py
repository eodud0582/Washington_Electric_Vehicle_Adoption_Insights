# ev_analysis_draft2.py

import pickle
import pandas as pd
import plotly.express as px
import streamlit as st

# Load data
@st.cache_data
def load_data():
    with open('MSU/Fall_2024/CMSE_830/midterm/data/ev.pickle', 'rb') as f:
        ev = pickle.load(f)
    with open('MSU/Fall_2024/CMSE_830/midterm/data/ev_merged.pickle', 'rb') as f:
        ev_merged = pickle.load(f)
    return ev, ev_merged

# Load data
ev, ev_merged = load_data()

# Introduction
st.markdown("""
# Electric Vehicle (EV) Registration Dashboard

**Target Audience:** Washington State Government and Automotive Industry Stakeholders

This dashboard shows the current status of electric vehicle (EV) registrations in Washington State. 
It explores the relationship between EV adoption, political trends, and infrastructure developments, including charging stations.
""")

# Basic statistics of the main EV dataset
st.markdown("## Basic EV Statistics")

st.write(ev.describe())

# Allow user to select legislative districts
districts = ev_merged['legislative_district'].unique()
selected_districts = st.sidebar.multiselect("Select Legislative District(s):", districts)

# Filter the EV data based on selected districts
if selected_districts:
    ev_filtered = ev[ev['legislative_district'].isin(selected_districts)]
    ev_merged_filtered = ev_merged[ev_merged['legislative_district'].isin(selected_districts)]
else:
    ev_filtered = ev
    ev_merged_filtered = ev_merged

# Visualize EV registration by type from the original dataset
fig_ev_type = px.bar(
    ev_filtered,  # Use the original ev dataset for this chart
    x='ev_type', 
    title='Electric Vehicle Registration by Type',
    labels={'ev_type': 'EV Type'},
    color='ev_type',
    color_discrete_sequence=px.colors.qualitative.Plotly
)

st.plotly_chart(fig_ev_type)

# Visualize EV registration by make
fig_ev_make = px.bar(
    ev_filtered, 
    x='make', 
    title='Electric Vehicle Registration by Maker',
    labels={'make': 'Maker'},
    color='make',
    color_discrete_sequence=px.colors.qualitative.Plotly
)

st.plotly_chart(fig_ev_make)

# Visualize EV registration by model year
fig_ev_model_year = px.histogram(
    ev_filtered, 
    x='model_year', 
    title='Electric Vehicle Registration by Model Year',
    labels={'model_year': 'Model Year'},
    color_discrete_sequence=px.colors.qualitative.Plotly
)

st.plotly_chart(fig_ev_model_year)

# Visualize EV registration by legislative district
fig_ev_district = px.bar(
    ev_filtered, 
    x='legislative_district', 
    title='Electric Vehicle Registration by Legislative District',
    labels={'legislative_district': 'Legislative District'},
    color='legislative_district',
    color_discrete_sequence=px.colors.qualitative.Plotly
)

st.plotly_chart(fig_ev_district)

# EV registration count by district
fig_ev_count = px.bar(
    ev_merged_filtered, 
    x='legislative_district', 
    y='ev_count', 
    color='party_won',
    title='EV Count by Legislative District',
    labels={'legislative_district': 'Legislative District', 'ev_count': 'EV Count'},
    color_discrete_sequence=['#3333FF', '#FF3333']
)

st.plotly_chart(fig_ev_count)

# Registered voters count by district
fig_registered_voters = px.bar(
    ev_merged_filtered, 
    x='legislative_district', 
    y='registered_voters',
    title='Registered Voters by Legislative District',
    labels={'legislative_district': 'Legislative District', 'registered_voters': 'Registered Voters'},
    color_discrete_sequence=['#66CDAA']
)

st.plotly_chart(fig_registered_voters)

# Charger count by district
fig_charger_count = px.bar(
    ev_merged_filtered, 
    x='legislative_district', 
    y='charger_count',
    title='Charger Count by Legislative District',
    labels={'legislative_district': 'Legislative District', 'charger_count': 'Charger Count'},
    color_discrete_sequence=['#FFA07A']
)

st.plotly_chart(fig_charger_count)

# Ratio of chargers to EVs by district
fig_charger_ev_ratio = px.bar(
    ev_merged_filtered, 
    x='legislative_district', 
    y='charger_ev_ratio',
    title='Charger to EV Ratio by Legislative District',
    labels={'legislative_district': 'Legislative District', 'charger_ev_ratio': 'Charger to EV Ratio'},
    color_discrete_sequence=['#FF6347']
)

st.plotly_chart(fig_charger_ev_ratio)

# Median household income by district
fig_income = px.bar(
    ev_merged_filtered, 
    x='legislative_district', 
    y='median_household_income',
    title='Median Household Income by Legislative District',
    labels={'legislative_district': 'Legislative District', 'median_household_income': 'Median Income'},
    color_discrete_sequence=['#9370DB']
)

st.plotly_chart(fig_income)

# Conclusion
st.markdown("""
## Conclusion

This dashboard shows the current status of electric vehicle registrations in Washington State. 
It highlights the relationship between EV registrations, political trends, and the availability of charging stations. 
This information is valuable for the Washington State government and automotive industry stakeholders to make informed decisions.
""")

# streamlit run MSU/Fall_2024/CMSE_830/midterm/ev_analysis_draft2.py

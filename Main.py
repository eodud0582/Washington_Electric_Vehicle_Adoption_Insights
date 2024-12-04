"""
MIT License

Copyright (c) 2024 Daeyoung Kim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import pandas as pd
import numpy as np
import pickle

import streamlit as st
# ================================== #
# Global setting

# Set page config
st.set_page_config(page_title="Washington State EV Adoption Analysis", page_icon=":battery:", layout="wide")
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

# Adjust sizes
st.markdown("""
    <style>
    /* Adjust the body font size */
    /* Reduces font size to 80% of default */
    html, body, [data-testid="stAppViewContainer"] {
        font-size: 80%;
    }

    /* Reduces the heading size */
    /* 
    h1, h2, h3, h4, h5, h6 {
        font-size: 100%;
    }
    */

    /* Scale down Plotly charts */
    /* 
    [data-testid="stPlotlyChart"] {
        transform: scale(0.8); 
    */
    }
    </style>
""", unsafe_allow_html=True)

highlight_color = '#0068C9'
unhighlight_color = 'lightgray'

# ================================== #
# Main page intro
st.title("Electric Vehicle Adoption in Washington State")
st.markdown("### Introduction")

st.divider()

st.markdown("")
col1, col2, col3 = st.columns([1,2,1])
with col1: st.write("")
with col2: 
    st.image("https://github.com/user-attachments/assets/a599e7a7-8468-4ba7-808b-95e71a799a87", 
             caption="Washington targets 100% electric vehicle sales by 2030 (Image created with the help of ChatGPT by OpenAI)")
    # st.markdown("<p style='text-align: center;'>(Image created with the help of ChatGPT by OpenAI)</p>", unsafe_allow_html=True)
with col3: st.write("")

st.markdown("")
st.markdown("""
This application explores the relationship between electric vehicle (EV) adoption in Washington State, economic factors, infrastructure developments, and political trends. The goal is to provide insights for policymakers, industry stakeholders, and researchers interested in promoting sustainable transportation.

**Designed for:**
- Washington State government policymakers
- Electric vehicle manufacturers and related industry professionals
- Policymakers and researchers from other states
""")

# Sidebar setting
st.sidebar.header("App User Guide")
st.sidebar.markdown("""
This application analyzes electric vehicle (EV) data and provides insights through predictive modeling.
""")

st.sidebar.info(
"""
Use the menu at the top left to navigate to the desired page.

1. **EV Analysis**: Analyze data and explore relevant insights.
2. **EV Prediction**: Predict EV Count by adjusting input variables and observe the impact of variable changes.
""")

# ================================== #
# Caching and initial data load
@st.cache_data
def load_data():
    """Load required data"""
    try:
        with open('data_processed/ev.pickle', 'rb') as f:
            ev = pickle.load(f)
        with open('data_processed/ev_merged.pickle', 'rb') as f:
            ev_merged = pickle.load(f)
        with open('data_processed/ev_state.pickle', 'rb') as f:
            ev_state = pickle.load(f)
        return ev, ev_merged, ev_state
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None
# The load_data() function is executed on the main page, caching the data and storing it in st.session_state
# Using @st.cache_data ensures the data load is cached, preventing repeated file reads

# Load data and store it in session_state
# - Sharing data across pages
# - All pages can reuse the data via st.session_state
if 'data_loaded' not in st.session_state:
    ev, ev_merged, ev_state = load_data()

    # Ensure data is loaded properly before proceeding
    if ev is None or ev_merged is None or ev_state is None:
        st.stop() # Stop the app if data loading fails
        
    st.session_state['ev'] = ev
    st.session_state['ev_merged'] = ev_merged
    st.session_state['ev_state'] = ev_state
    st.session_state['data_loaded'] = True # Set a flag to ensure data is loaded only once

# ================================== #
# Add a sidebar for additional information or controls
st.sidebar.header("Data Sources")
st.sidebar.markdown("""
- Electric Vehicle Registrations by State
- Electric Vehicle Population Data (Washington)
- 2022 Washington State Legislative Election Results
- Alternative Fuel Stations (Charging Stations)
- Median Household Income (ACS 2022 5-year)
- Washington State Legislative Districts 2022 (Geospatial)
""")
# - Electric Vehicle Registration Counts by State
# - Electric Vehicle Population in Washington State
# - General Election Results in Washington State 2022
# - Alternative Fuel Stations in Washington State
# - Median Household Income in Washington State 2022
# - Washington State Legislative Districts 2022 (Geospatial)

# ================================== #
# Additional information about the project
st.divider()

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("### Insights by Daeyoung Kim")
    st.write(
        "Email: kimdae15@msu.edu | [GitHub](https://github.com/eodud0582) | [LinkedIn](https://linkedin.com/in/eodud0582)"
    )
with col2:
    st.markdown("### License")
    st.write("MIT")

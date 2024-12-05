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

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor

import shap
import altair as alt
import streamlit as st
from streamlit.components.v1 import html
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
red_color = '#D32F2F'

# ================================== #
# Intro
st.title("Electric Vehicle Adoption in Washington State")
st.markdown("### Electric Vehicle Count Prediction")

st.divider()

st.write("This tool allows you to predict EV count and explore the effect of key variable on predictions.")

# Load data
if 'data_loaded' in st.session_state and st.session_state['data_loaded']:
    ev = st.session_state['ev']
    ev_merged = st.session_state['ev_merged']
    ev_state = st.session_state['ev_state']
else:
    st.warning("Data has not been loaded. Please load the data on the main page.")
    st.stop()

# Load model and scaler
with open('data_processed/final_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
    model = loaded_model['model']
    scaler = loaded_model['scaler']
    selected_features = loaded_model['selected_features']

# ================================== #
# User input setting

# User input (new test data)
st.sidebar.header("Input Variables")
income = st.sidebar.slider(
    "Median Household Income", # Label for input slider
    float(ev_merged['median_household_income'].min()), # Minimum value for slider
    float(ev_merged['median_household_income'].max()), # Maximum value for slider
    float(ev_merged['median_household_income'].mean()), # Default value (mean)
    step=1.0 # Step size for slider
)
dem_votes = st.sidebar.slider(
    "Democratic Party Support (Votes)",
    float(ev_merged['dem_votes'].min()),
    float(ev_merged['dem_votes'].max()),
    float(ev_merged['dem_votes'].mean()),
    step=1.0
)
rep_votes = st.sidebar.slider(
    "Republican Party Support (Votes)",
    float(ev_merged['rep_votes'].min()),
    float(ev_merged['rep_votes'].max()),
    float(ev_merged['rep_votes'].mean()),
    step=1.0
)
charger_density_scaled = st.sidebar.slider(
    "Charger Density (scaled, x10⁹)",
    float(ev_merged['charger_density'].min() * 1e9), # Minimum value, scaled
    float(ev_merged['charger_density'].max() * 1e9), # Maximum value, scaled
    float(ev_merged['charger_density'].mean() * 1e9), # Default value (mean), scaled
    step=0.1
)
charger_density = charger_density_scaled / 1e9 # Convert scaled input back to original unit
margin_error = ev_merged['margin_error'].mean() # Use the mean value for margin error (fixed/constant for simplicity)

# Create input data
original_input = pd.DataFrame({
    'median_household_income': [income], # User input for household income
    'margin_error': [margin_error], # Constant value for margin error
    'dem_votes': [dem_votes], # User input for Democratic votes
    'rep_votes': [rep_votes], # User input for Republican votes
    'charger_density': [charger_density] # User input for charger density, converted to original unit
})

# Verify selected variables
assert list(original_input.columns) == selected_features, "Feature names do not match expected names!"

col1, col2 = st.columns(2)
with col1:
    # 1) EV count prediction
    scaled_input = scaler.transform(original_input[selected_features])
    original_prediction = model.predict(scaled_input)[0] # ev_count (original value)
    
    # Prediction
    st.write("### Predicted Electric Vehicle Count")
    st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; height: 100%; min-height: 150px;">
        <h1 style="color: #0068C9; font-weight: bold;">{:.2f}</h1>
    </div>
    """.format(original_prediction),
    unsafe_allow_html=True
    )
with col2:
    # 2) Feature Importance
    st.write("### Key Features and Importance")
    
    # Feature Importance (from the Gradient Boosting Model)
    fi_features = [col for col in selected_features if col != 'margin_error']
    feature_importance = pd.DataFrame({
        'Feature': fi_features,
        'Importance': model.feature_importances_[np.where(np.isin(selected_features, fi_features))] # Extracted from the model trained with the entire dataset
    }).sort_values(by='Importance', ascending=False)
    
    # Altair chart
    chart = alt.Chart(feature_importance).mark_bar(color=highlight_color).encode(
        x=alt.X('Importance', title='Importance'), # Importance values
        y=alt.Y('Feature', sort='-x', title='Feature'), # Lists the features, sorted by importance
        tooltip=['Feature', 'Importance']
    ).properties(
        width='container', # Adaptive width
        height=160 # Height for clarity
    )
    
    st.altair_chart(chart, use_container_width=True)

# ================================== #
# Evaluate effect of variable/variable changes

# 1) Simulation: effect of variable changes
# simulation_results = []
# for feature in selected_features:
#     modified_input = original_input.copy()
    
#     # Set up increase/decrease for the variable
#     change_amount = (original_input[feature][0] + 1.0) # 10% change or a minimum of 1.0
    
#     modified_input[feature] = original_input[feature] + change_amount
#     increased_scaled = scaler.transform(modified_input)
#     increased_prediction = model.predict(increased_scaled)[0]
    
#     modified_input[feature] = original_input[feature] - change_amount
#     decreased_scaled = scaler.transform(modified_input)
#     decreased_prediction = model.predict(decreased_scaled)[0]
    
#     simulation_results.append({
#         "Variable": feature,
#         "Input Value": original_input[feature][0],
#         "Original Prediction": original_prediction,
#         "Increased Prediction": increased_prediction,
#         "Increased Effect": increased_prediction - original_prediction,
#         "Decreased Prediction": decreased_prediction,
#         "Decreased Effect": decreased_prediction - original_prediction
#     })

# Create simulation table
# simulation_df = pd.DataFrame(simulation_results)

# st.write("### Simulation: Effect of Variable Changes")
# st.table(simulation_df)

# ---
# 2) SHAP

# SHAP Explainer Initialization
explainer = shap.Explainer(model, feature_names=selected_features)

# Compute SHAP values for the scaled input
shap_values = explainer(scaled_input)

# Display SHAP results in two columns
col1, col2 = st.columns(2)
with col1:
    # Display a table summarizing SHAP values
    st.write("### Variable Impact Analysis (SHAP Values)")
    shap_table = pd.DataFrame({
        'Variable': selected_features,
        'Impact Score': shap_values.values[0]
    }).sort_values(by='Impact Score', ascending=False).reset_index(drop=True) #.to_dict(orient='records')
    st.table(shap_table)
    # st.dataframe(shap_table, hide_index=True)
with col2:
    # Generate SHAP force plot (interactive visualization)
    st.write("### Variable Impact Direction (SHAP Force Plot)")
    force_plot_html = shap.force_plot(
        explainer.expected_value,
        shap_values.values[0],
        feature_names=selected_features,
        matplotlib=False, # Render as HTML
        plot_cmap=[red_color, highlight_color]
    )
    # Embed the SHAP force plot in Streamlit using an iframe
    # - Rendering shap.force_plot as an HTML plot in Streamlit requires wrapping it in an iframe. 
    # - Streamlit doesn't natively support direct HTML rendering for SHAP visualizations.
    # - Need to save the force plot as an interactive HTML snippet and embed it using st.components.v1.html.
    shap_html = f"<head>{shap.getjs()}</head><body>{force_plot_html.html()}</body>"
    html(shap_html, height=160)

# st.write("### SHAP Waterfall Plot")
# shap.waterfall_plot(shap_values[0], feature_names=selected_features)

# ================================== #
# SHAP explanation
st.markdown(
    """
    **SHAP (SHapley Additive exPlanations)** helps understand how each input variable (feature) impacts the model's prediction.
    """
    )
col1, col2 = st.columns(2)
with col1:
    st.markdown(
    """
    **Understanding SHAP Values and Force Plot**
    
    **Base Value:**
    - This is the starting point or the average prediction if no specific features are considered.
    - Imagine it as the model's "default" prediction based on the overall dataset.
    
    **SHAP Values:**
    - SHAP values measure how much each feature "pushes" the prediction higher or lower compared to the base value.
    - Positive SHAP values push the prediction higher, while negative values pull it lower.
    
    **Force Plot:**
    - The force plot is a visual way to see how each feature contributes to the prediction.
    - Features in red increase the prediction, and features in blue decrease it.
    - The total prediction is the base value + all SHAP values.
    """
    )
with col2:
    st.markdown(
    """
    **How to Read the Force Plot**
    - **Red (Left Side):** Indicates features that increase the model's prediction.
    - **Blue (Right Side):** Indicates features that decrease the model's prediction.
    - **Base Value (Middle):** The starting prediction before considering individual feature contributions.
    
    **Insights Example**
    - If the base value is 50, and one feature increases the prediction by 10 while another decreases it by 5, the final prediction will be 55 (50 + 10 - 5).
    - **`median_household_income`**, **`dem_votes`**, and **`rep_votes`** contribute to the **red region**, indicating they increase the prediction.
    - **`margin_error`** is observed in the **blue region**, suggesting it decreases the prediction.
    - The length of the bars represents the magnitude of each feature's impact:
        - **`median_household_income`** and **`dem_votes`** generally have longer bars, showing they have a strong influence on the prediction.
        - **`margin_error`** also has a significant bar length, indicating its notable impact despite being in the blue region.
    """
    )
# ================================== #
# Add a sidebar for additional information or controls
st.sidebar.header("Usage Guide")
st.sidebar.markdown("""
- Use sliders to adjust key input variables.
- Observe real-time EV count predictions.
- Examine SHAP values to understand feature impacts.
- Experiment with different scenarios to explore potential EV adoption trends.
""")

st.sidebar.header("About This Tool")
st.sidebar.info("This predictive tool enables you to explore electric vehicle (EV) adoption in Washington State by:"\
                "\n- Predicting EV count based on key economic and infrastructure variables."\
                "\n- Allowing interactive adjustment of input parameters."\
                "\n- Visualizing the impact of individual features on EV predictions using SHAP analysis.")

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

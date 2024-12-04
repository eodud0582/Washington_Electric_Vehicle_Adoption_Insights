import streamlit as st
import altair as alt

import pandas as pd
import numpy as np
import pickle

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler

import shap
from streamlit.components.v1 import html

# ================================== #
# Global setting

# Set page config
st.set_page_config(page_title="Washington State EV Adoption Analysis", page_icon=":battery:", layout="wide")
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

# st.set_page_config(page_title="EV Count Prediction", layout="wide")

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
# Intro
st.title("Electric Vehicle Adoption in Washington State")
st.markdown("### EV Count Prediction")

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

# @st.cache_data
# def load_or_train_model():
#     """Load a pre-trained model or train a new one."""
#     try:
#         # Try to load the saved model
#         with open('best_model_gbr.pkl', 'rb') as f:
#             model = pickle.load(f)
#     except FileNotFoundError:
#         # Train the model if not already saved
#         # data, _, _ = load_processed_data()
#         X = ev_merged[['median_household_income', 'dem_votes', 'margin_error']]
#         y = ev_merged['ev_count']
#         model = GradientBoostingRegressor(n_estimators=500, random_state=777)
#         model.fit(X, y)
#         # Save the trained model
#         with open('best_model_gbr.pkl', 'wb') as f:
#             pickle.dump(model, f)
#     return model
# model = load_or_train_model()
# def prepare_scaler_and_model(data):
#     """Fit scaler and train the final model on all data."""
#     X = data[['median_household_income', 'dem_votes', 'margin_error']]
#     y = data['ev_count']
#     # Fit the scaler on all data
#     scaler = StandardScaler()
#     X_scaled = scaler.fit_transform(X)
#     # Train the final model on scaled data
#     model = GradientBoostingRegressor(n_estimators=500, random_state=777)
#     model.fit(X_scaled, y)
#     return scaler, model
# scaler, model = prepare_scaler_and_model(ev_merged)

# 모델과 스케일러 로드
with open('MSU/Fall_2024/CMSE_830/project/final_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
    model = loaded_model['model']
    scaler = loaded_model['scaler']
    selected_features = loaded_model['selected_features']

# ================================== #
# Input setting

# 사용자 입력 받기 (새로운 테스트 데이터)
# 입력된 데이터를 스케일링한 후 학습된 모델에 전달하므로, 완전히 새로운 데이터를 예측하는 과정
st.sidebar.header("Input Variables")
income = st.sidebar.slider(
    "Median Household Income",
    float(ev_merged['median_household_income'].min()),
    float(ev_merged['median_household_income'].max()),
    float(ev_merged['median_household_income'].mean()),
    step=1.0
)
dem_votes = st.sidebar.slider(
    "Democratic Party Votes",
    float(ev_merged['dem_votes'].min()),
    float(ev_merged['dem_votes'].max()),
    float(ev_merged['dem_votes'].mean()),
    step=1.0
)
rep_votes = st.sidebar.slider(
    "Republican Party Votes",
    float(ev_merged['rep_votes'].min()),
    float(ev_merged['rep_votes'].max()),
    float(ev_merged['rep_votes'].mean()),
    step=1.0
)
charger_density_scaled = st.sidebar.slider(
    "Charger Density (scaled, x10⁹)",
    float(ev_merged['charger_density'].min() * 1e9),  # 최소값 스케일 조정
    float(ev_merged['charger_density'].max() * 1e9),  # 최대값 스케일 조정
    float(ev_merged['charger_density'].mean() * 1e9),  # 평균값 스케일 조정
    step=0.1
)
charger_density = charger_density_scaled / 1e9  # 원래 단위로 변환
margin_error = ev_merged['margin_error'].mean()  # Fixed constant for simplicity

# 입력 데이터 생성
original_input = pd.DataFrame({
    'median_household_income': [income],
    'margin_error': [margin_error],
    'dem_votes': [dem_votes],
    'rep_votes': [rep_votes],
    'charger_density': [charger_density]
})

# 선택된 변수 검증
# expected_feature_names = ['median_household_income', 'margin_error', 'dem_votes', 'rep_votes', 'charger_density']
assert list(original_input.columns) == selected_features, "Feature names do not match expected names!"

col1, col2 = st.columns(2)
with col1:
    # 1. EV count prediction
    scaled_input = scaler.transform(original_input[selected_features])
    original_prediction = model.predict(scaled_input)[0] # target인 ev_count는 애초에 원 값임
    
    # Prediction 결과 표시
    st.write("### Predicted EV Count")
    # st.markdown(
    #     f"<h1 style='text-align: center; color: #0068C9;'><b>{original_prediction:.2f}</b></h1>",
    #     unsafe_allow_html=True
    # )
    st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; height: 100%; min-height: 200px;">
        <h1 style="color: #0068C9; font-weight: bold;">{:.2f}</h1>
    </div>
    """.format(original_prediction),
    unsafe_allow_html=True
    )
with col2:
    # 2. Feature Importance
    st.write("### Feature Importance")
    
    # Feature Importance (from the Gradient Boosting Model)
    fi_features = [col for col in selected_features if col != 'margin_error']
    feature_importance = pd.DataFrame({
        'Feature': fi_features,
        'Importance': model.feature_importances_[np.where(np.isin(selected_features, fi_features))] # 표시된 변수 중요도는 최종 학습된 모델 기준
    }).sort_values(by='Importance', ascending=False)
    
    # Altair chart
    chart = alt.Chart(feature_importance).mark_bar(color=highlight_color).encode(
        x=alt.X('Importance', title='Importance'),
        y=alt.Y('Feature', sort='-x', title='Feature'),  # 중요도 순서로 정렬
        tooltip=['Feature', 'Importance']
    ).properties(
        width=600,  # 너비 설정
        height=200  # 높이 설정
    )
    
    st.altair_chart(chart, use_container_width=True)

# ================================== #
# Evaluate effect of variable/variable changes

# Simulation: effect of variable changes
# 1)
# 시뮬레이션 테이블 생성
# simulation_results = []
# for feature in selected_features:
#     modified_input = original_input.copy()
    
#     # 변수 증가/감소 설정
#     change_amount = (original_input[feature][0] + 1.0)  # 10% 변화 또는 최소 1.0
    
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

# simulation_df = pd.DataFrame(simulation_results)

# # Simulation 결과 테이블 표시
# st.write("### Simulation: Effect of Variable Changes")
# st.table(simulation_df)

# 2) SHAP

# SHAP 해석기 초기화
explainer = shap.Explainer(model, feature_names=selected_features)

# SHAP 값 계산
shap_values = explainer(scaled_input)

col1, col2 = st.columns(2)
with col1:
    # SHAP Summary Plot
    st.write("### Variable Impact Analysis (SHAP Values)")
    shap_table = pd.DataFrame({
        'Variable': selected_features,
        'SHAP Value': shap_values.values[0]
    }).sort_values(by='SHAP Value', ascending=False)
    st.table(shap_table)
with col2:
    # 전체 SHAP Force Plot (시각적 요약 제공) 생성 및 HTML 렌더링
    st.write("### SHAP Force Plot")
    force_plot_html = shap.force_plot(
        explainer.expected_value,
        shap_values.values[0],
        feature_names=selected_features,
        matplotlib=False,  # HTML로 렌더링
        # plot_cmap=["#000000", highlight_color]
    )
    # HTML로 Streamlit에 표시
    shap_html = f"<head>{shap.getjs()}</head><body>{force_plot_html.html()}</body>"
    html(shap_html, height=200)

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
    Understanding SHAP Values and Force Plot
    
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
    How to Read the Force Plot
    - Blue (Right Side): Indicates features that decrease the model's prediction
    - Red (Left Side): Indicates features that increase the model's prediction
    - Base Value (Middle): The starting prediction before considering individual feature contributions
    
    Example:
    - If the base value is 50, and one feature increases the prediction by 10 while another decreases it by 5, the final prediction will be 55 (50 + 10 - 5).
    
    """
    )
# ================================== #
# Add a sidebar for additional information or controls

st.sidebar.header("Usage Guide")
st.sidebar.markdown("""
- Use sliders to adjust key input variables
- Observe real-time EV count predictions
- Examine SHAP values to understand feature impacts
- Experiment with different scenarios to explore potential EV adoption trends
""")

st.sidebar.header("About This Tool")
st.sidebar.info("This predictive tool enables you to explore electric vehicle (EV) adoption in Washington State by:"\
                "\n- Predicting EV count based on key economic and infrastructure variables"\
                "\n- Allowing interactive adjustment of input parameters"\
                "\n- Visualizing the impact of individual features on EV predictions using SHAP analysis")

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
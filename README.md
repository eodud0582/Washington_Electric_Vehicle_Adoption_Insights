# Washington Electric Vehicle (EV) Adoption Insights App
---

<p align="center">
  <img src="https://github.com/user-attachments/assets/a599e7a7-8468-4ba7-808b-95e71a799a87" style="width:60%" alt="washington ev">
</p>
<p align="center" style="font-size: 6px; margin-top: 1px;">
  Washington targets 100% electric vehicle sales by 2030 <br>
  (Image created with the help of ChatGPT by OpenAI)
</p>

## Problem Definition and App Purpose

**Washington State** is at the forefront of **electric vehicle (EV) adoption** in the United States. With an ambitious goal of achieving 100% EV sales by 2030, the state government has implemented various incentives and policies to promote EV adoption. This commitment has resulted in one of the fastest-growing EV registration rates nationwide.

Despite this progress, understanding the driving factors behind EV adoption and forecasting future trends remains a complex challenge. Key questions arise, such as:
- What economic, infrastructural, or political factors most significantly influence EV adoption?
- How can policymakers adjust these variables to meet ambitious EV adoption targets?
- What insights can Washington State's data offer to other states or stakeholders in the EV industry?

This app aims to provide actionable insights and predictive tools to address these questions. Through a combination of detailed analysis and an interactive prediction service, this app helps users:
- Understand the factors driving EV adoption in Washington State.
- Evaluate how changes in key variables can influence EV registration trends.
- Leverage Washington State's leadership in the EV market to inform strategies for other regions and industries.

## About the App

This **Washington EV Adoption Insights** app provides a detailed analysis of EV adoption in Washington State, exploring its relationship with economic indicators, infrastructure development, and political factors. Additionally, a prediction feature allows you to customize key variables, observe their interactions, and evaluate how changes impact the outcomes.

This app is designed for:
- **Policymakers** looking to make informed decisions about EV promotion.
- **Industry stakeholders** seeking insights into market trends.
- **Researchers and other states** aiming to understand the key factors driving EV adoption.

## Key Features
- **EV Adoption Overview**: Analyze the distribution of electric vehicles across Washington State. <!-- and compare it with other U.S. states -->
- **Economic Insights**: Understand how median household income relates to EV adoption rates.
- **Infrastructure Analysis**: Explore the relationship between EV adoption and the availability of charging infrastructure.
- **Political Landscape**: See how EV adoption correlates with political trends and legislative districts.
- **Customizable Filters**: Users can select different legislative districts for a more tailored analysis.
- **Chart Options**: Within some major topics, users can choose from various chart types to gain deeper insights.
- **Prediction**: Adjust input variables to predict EV registrations and assess the influence of key factors.

## How to Access the App

This app has been deployed on **Streamlit** and is publicly accessible. You can view it by simply visiting the following link:

[https://evwash.streamlit.app](https://evwash.streamlit.app/)

## How to Run the App Locally

This app is built with **Streamlit**, a tool that allows you to easily create interactive dashboards and web apps in Python. Follow these steps to run the app locally on your machine.

### 1) Prerequisites

<details>
<summary><strong>Click here to view the prerequisites</strong></summary>
<br>

  Python installed:
  - Python 3.12.6
  
  Packages installed:
  - pandas 2.2.3
  - numpy 1.26.4
  - statsmodels 0.14.2
  - matplotlib 3.9.3
  - plotly 5.24.1
  - scikit-learn 1.5.2
  - shap 0.46.0
  - streamlit 1.38.0
  - streamlit-shap

</details>

### 2) Step-by-Step Instructions

<details>
<summary><strong>Click here to view the instructions</strong></summary>
<br>

**a) Clone the repository**
   
   First, clone this repository to your local machine:
   
   ```
   git clone https://github.com/eodud0582/Washington_State_Electric_Vehicle_Adoption_Analysis.git
   cd Washington_State_Electric_Vehicle_Adoption_Analysis
   ```

**b) Create and activate a virtual environment (optional but recommended)**
   
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

**c) Install required packages**
   
   The easiest way to install the necessary packages is by using the `requirements.txt` file::
   
   ```
   pip install -r requirements.txt
   ```

   Alternatively, you can manually install the packages:

   ```
   pip install pandas==2.2.3 numpy==1.26.4 statsmodels==0.14.2 plotly==5.24.1 streamlit==1.38.0
   ```

**d) Download the data**
   
   Ensure the data files (`ev.pickle`, `ev_merged.pickle`, `ev_state.pickle`) are available in the `data_processed/` folder.
   If these files are not included in the repository due to size limits, you will need to manually download or provide these files.

**e) Run the Streamlit app**
   
   Once everything is set up, you can launch the Streamlit app by running the following command:

   ```
   streamlit run ev_analysis_streamlit.py
   ```

**f) Access the app**
    
   After running the command, the Streamlit app will automatically open in your browser on `http://localhost:8501`. Otherwise, a local URL will be provided in the terminal. Open that link in your browser to view and interact with the app.
  
</details>

## App Structure

```
Washington_State_Electric_Vehicle_Adoption_Analysis/
│
├── Main.py                   # Main entry point for launching the Streamlit app
├── pages/                    # Contains individual pages for analysis and prediction functionalities
│   └── 0_Dataset.py          # Python file for data sources, cleaning process, and feature engineering overview
│   └── 1_EV_Analysis.py      # Python file for the analysis dashboard
│   └── 2_EV_Prediction.py    # Python file for the prediction service
├── data_processed/           # Contains processed datasets in pickle format, ready for analysis and prediction
│   └── ev.pickle             # Primary raw dataset on electric vehicle population in Washington state
│   └── ev_state.pickle       # Dataset on electrical vehicle population by state
│   └── ev_merged.pickle      # Preprocessed and merged dataset with features for analysis and prediction
├── .streamlit/               # Folder containing a Streamlit configuration file
│   └── config.toml           # Streamlit configuration
├── requirements.txt          # List of Python packages required to run the app
├── README.md                 # App overview and instructions (this file)
└── assets/                   # Folder for static files like images or additional resources
```

## Data Sources

This app leverages the following data:
1. [**Electric Vehicle Registrations by State**](https://afdc.energy.gov/data/10962)
2. [**Washington State Electric Vehicle Population Data**](https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2/about_data)
3. [**Washington State 2022 Legislative Election Results**](https://www.kaggle.com/datasets/josephdemey/2022-washington-state-legislative-election-results)
4. [**Washington State Alternative Fuel Stations (Charging Stations)**](https://afdc.energy.gov/data_download)
5. [**Washington State Median Household Income (ACS 2022 5-year)**](https://censusreporter.org/data/table/?table=B19013&geo_ids=610|04000US53#)
6. [**Washington State Legislative Districts 2022 (Geospatial)**](https://geo.wa.gov/datasets/c2b31e7e2b6f464a92d1bed7ab1d7539_0/explore?location=47.056733%2C-120.812244%2C7.15)
7. [**Washington State Voter Demographics Tables (Age)**](https://www.sos.wa.gov/elections/data-research/election-data-and-maps/reports-data-and-statistics/voter-demographics)

## Data Cleaning and Processing

These datasets were cleaned and processed through the following steps:
- **Filtering Washington-specific data**: Removed data unrelated to Washington State to maintain focus.
- **Handling missing values through imputation**: Addressed missing values using logical assumptions and patterns in the data.
- **Feature engineering**: Created new variables to enhance analysis and derive meaningful insights.

### Variables Created and Used

<div style="overflow-x: auto;">  
  <details>
  <summary><strong>Click here to view the variables</strong></summary>
  <br>
    
  | Variable                     | Description                                           |
  |------------------------------|-------------------------------------------------------|
  | `legislative_district`        | Washington State legislative district ID              |
  | `ev_count`                   | Number of electric vehicles (EVs)                     |
  | `registered_voters`           | Total registered voters in the district               |
  | `ballots_cast`                | Number of ballots cast in the latest election         |
  | `%_turnout`                   | Voter turnout percentage                             |
  | `dem_votes`                | Votes received by candidate Patty Murray (Democratic)            |
  | `rep_votes`              | Votes received by candidate Tiffany Smiley (Republican)          |
  | `party_won`                   | Party that won in the district                       |
  | `charger_count`               | Total number of EV chargers                          |
  | `geoid`                       | Unique geographic identifier for the district        |
  | `median_household_income`     | Median household income in the district              |
  | `margin_error`                | Margin of error for household income estimates       |
  | `shape_leng`                  | Length of the district boundary                      |
  | `shape_le_1`                  | Additional measure of district boundary length       |
  | `shape_area`                  | Total area of the district                           |
  | `shape__area`                 | Alternative measure for district area                |
  | `shape__length`               | Alternative measure for district boundary length     |
  | `voters_18_24`               | Number of registered voters aged 18–24               |
  | `voters_25_34`               | Number of registered voters aged 25–34               |
  | `voters_35_44`               | Number of registered voters aged 35–44               |
  | `voters_45_54`               | Number of registered voters aged 45–54               |
  | `voters_55_64`               | Number of registered voters aged 55–64               |
  | `voters_over_65`             | Number of registered voters aged 65+                 |
  | `total_active_voters`        | Total number of active voters in the district        |
  | `charger_density`             | EV charger density per unit of area (shape_area-based) |
  | `charger_density__area`      | Alternative measure of charger density per unit of area (shape__area-based) |
  | `charger_density_leng`       | EV charger density relative to boundary length (shape_leng-based) |
  | `charger_density_le_1`       | Alternative measure of charger density relative to boundary length (shape_le_1-based) |
  | `charger_density__length`    | Additional measure of charger density relative to boundary length (shape__length-based) |
  | `charger_per_voter_total`    | Chargers per total registered voters                 |
  | `charger_per_voter_18_24`    | Chargers per voter aged 18–24                        |
  | `charger_per_voter_25_34`    | Chargers per voter aged 25–34                        |
  | `charger_per_voter_35_44`    | Chargers per voter aged 35–44                        |
  | `charger_per_voter_45_54`    | Chargers per voter aged 45–54                        |
  | `charger_per_voter_55_64`    | Chargers per voter aged 55–64                        |
  | `charger_per_voter_over_65`  | Chargers per voter aged 65+                          |
  | `charger_ev_ratio`            | Ratio of EV chargers to EVs                          |
  | `transformed_ev_count`        | Transformed number of EVs for analysis               |
  | `transformed_charger_count`   | Transformed number of chargers for analysis          |
  | `transformed_charger_ev_ratio`| Transformed charger-to-EV ratio for analysis         |
  | `transformed_charger_density` | Transformed charger density for analysis             |
    
  </details>
</div>

## Acknowledgements

Special thanks to the open data sources and tools that made this analysis possible. This app was built using:
- **Streamlit** for the interactive web app.
- **Plotly** and **Altair** for visualizing data in dynamic, interactive plots.
- **Pandas** and **NumPy** for data manipulation and analysis.
- **Scikit-Learn** for predictive modeling.
- **SHAP** for model explanation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

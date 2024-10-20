# Washington State Electric Vehicle (EV) Adoption Analysis
---

<p align="center">
  <img src="https://github.com/user-attachments/assets/a599e7a7-8468-4ba7-808b-95e71a799a87" style="width:60%" alt="washington ev">
</p>
<p align="center" style="font-size: 6px; margin-top: 1px;">
  Washington targets 100% electric vehicle sales by 2030 <br>
  (Image created with the help of ChatGPT by OpenAI)
</p>

Welcome to the **Washington State Electric Vehicle (EV) Adoption Analysis** project! This dashboard provides a detailed analysis of EV adoption in Washington State, exploring its relationship with economic indicators, infrastructure development, and political factors.

This analysis is designed for:
- **Policymakers** looking to make informed decisions about EV promotion.
- **Industry stakeholders** seeking insights into market trends.
- **Researchers and other states** aiming to understand the key factors driving EV adoption.

## 1. Key Features
- **EV Adoption Overview**: Analyze the distribution of electric vehicles across Washington State and compare it with other U.S. states.
- **Economic Insights**: Understand how median household income relates to EV adoption rates.
- **Infrastructure Analysis**: Explore the relationship between EV adoption and the availability of charging infrastructure.
- **Political Landscape**: See how EV adoption correlates with political trends and legislative districts.
- **Customizable Filters**: Users can select different legislative districts for a more tailored analysis.
- **Chart Options**: Within some major topics, users can choose from various chart types to gain deeper insights.

## 2. How to Access the Dashboard

This dashboard is deployed and can be accessed at:
- https://waevanalysis.streamlit.app

## 3. How to Run the Dashboard Locally

This project is built with **Streamlit**, a tool that allows you to easily create interactive dashboards and web apps in Python. Follow these steps to run the dashboard locally on your machine.

### 1) Prerequisites

Python installed:
- Python 3.12.6

Packages installed:
- pandas 2.2.3
- numpy 1.26.4
- statsmodels 0.14.2
- plotly 5.24.1
- streamlit 1.38.0

### 2) Step-by-Step Instructions

Once the requirements are met, follow these steps:

<details>
<summary><strong>Click here to expand the instructions</strong></summary>
<br>

a) **Clone the repository**
   
   First, clone this repository to your local machine:
   
   ```
   git clone https://github.com/eodud0582/Washington_State_Electric_Vehicle_Adoption_Analysis.git
   cd Washington_State_Electric_Vehicle_Adoption_Analysis
   ```

b) **Create and activate a virtual environment (optional but recommended)**
   
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

c) **Install required packages**
   
   The easiest way to install the necessary packages is by using the `requirements.txt` file::
   
   ```
   pip install -r requirements.txt
   ```

   Alternatively, you can manually install the packages:

   ```
   pip install pandas==2.2.3 numpy==1.26.4 statsmodels==0.14.2 plotly==5.24.1 streamlit==1.38.0
   ```

d) **Download the data**
   
   Ensure the data files (`ev.pickle`, `ev_merged.pickle`, `ev_state.pickle`) are available in the `data_processed/` folder.
   If these files are not included in the repository due to size limits, you will need to manually download or provide these files.

e) **Run the Streamlit app**
   
   Once everything is set up, you can launch the Streamlit app by running the following command:

   ```
   streamlit run ev_analysis_streamlit.py
   ```

f) **Access the dashboard**
    
   After running the command, the Streamlit dashboard will automatically open in your browser on `http://localhost:8501`. Or, a local URL will be provided in the terminal. Open that link in your browser to view and interact with the dashboard.
  
</details>


### 3) Project Structure

```
Washington_State_Electric_Vehicle_Adoption_Analysis/
│
├── ev_analysis_streamlit.py  # Main Python file for Streamlit app
├── data_processed/           # Folder containing the processed data files in pickle format
├── .streamlit/
│   └── config.toml           # Streamlit configuration
├── requirements.txt          # Python packages
└── README.md                 # Project overview and instructions (this file)
```

## 4. Data Sources

This dashboard leverages the following data:
- **Electric Vehicle Population in Washington State**
- **Washington State General Election Results 2022**
- **Alternative Fuel Stations in Washington (Charging Stations)**
- **Median Household Income by Legislative District**
- **Electric Vehicle Registration Counts by State**
- **Washington State Legislative Districts 2022 (Geospatial Info)**

These datasets have been merged, feature-engineered, and transformed into the following variables:

<div style="overflow-x: auto;">  
  <details>
  <summary><strong>Click here to expand the table</strong></summary>
  <br>
    
  | Variable                     | Description                                           |
  |------------------------------|-------------------------------------------------------|
  | `legislative_district`        | Washington State legislative district ID              |
  | `ev_count`                   | Number of electric vehicles (EVs)                     |
  | `registered_voters`           | Total registered voters in the district               |
  | `ballots_cast`                | Number of ballots cast in the latest election         |
  | `%_turnout`                   | Voter turnout percentage                             |
  | `patty_murray`                | Votes received by candidate Patty Murray             |
  | `tiffany_smiley`              | Votes received by candidate Tiffany Smiley           |
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
  | `charger_density`             | Density of EV chargers in the district               |
  | `charger_density_per_100`     | Charger density per 100 square miles                 |
  | `charger_ev_ratio`            | Ratio of EV chargers to EVs                          |
  | `party_won_encoded`           | Encoded value of the winning party                   |
  | `transformed_ev_count`        | Transformed number of EVs for analysis               |
  | `transformed_charger_count`   | Transformed number of chargers for analysis          |
  | `transformed_charger_ev_ratio`| Transformed charger-to-EV ratio for analysis         |
  | `transformed_charger_density` | Transformed charger density for analysis             |
    
  </details>
</div>

## 5. Acknowledgements

Special thanks to the open data sources and tools that made this analysis possible. This project was built using:
- **Streamlit** for the interactive web app.
- **Plotly** for visualizing data in dynamic, interactive plots.
- **Pandas** and **NumPy** for data manipulation and analysis.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

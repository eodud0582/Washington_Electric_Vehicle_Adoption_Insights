# Washington State Electric Vehicle (EV) Adoption Analysis
---

Welcome to the **Washington State Electric Vehicle (EV) Adoption Analysis** project! This dashboard provides a detailed analysis of EV adoption in Washington State, examining trends in relation to political factors, economic indicators, and infrastructure development.

This analysis is designed for:
- **Policymakers** looking to make informed decisions about EV promotion.
- **Industry stakeholders** seeking insights into market trends.
- **Researchers and other states** aiming to understand the key factors driving EV adoption.

## Key Features
- **EV Adoption Overview**: Analyze the distribution of electric vehicles across Washington State and compare it with other U.S. states.
- **Economic Insights**: Understand how median household income relates to EV adoption rates.
- **Infrastructure Analysis**: Explore the relationship between EV adoption and the availability of charging infrastructure.
- **Political Landscape**: See how EV adoption correlates with political trends and legislative districts.
- **Customizable Filters**: Users can select different legislative districts for a more tailored analysis.

## Running the Streamlit App

This project is built with **Streamlit**, a tool that allows you to easily create interactive dashboards and web apps in Python. Follow these steps to run the dashboard locally on your machine.

### Prerequisites

Before you start, make sure you have the following installed:
- **Python 3.7 or higher**
- Required Python packages listed in `requirements.txt`.

### Step-by-Step Instructions

1. **Clone the repository**:  
   First, clone this repository to your local machine:
   ```bash
   git clone https://github.com/eodud0582/ev-adoption-washington.git
   cd ev-adoption-washington
   ```

2. **Install dependencies**:  
   Next, install the required Python packages. You can use the `requirements.txt` file to do this easily:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the data**:  
   Make sure the data files (`ev.pickle`, `ev_merged.pickle`, `ev_state.pickle`) are available in the `data/` folder. If not included in the repo due to size limits, you'll need to provide these files.

4. **Run the Streamlit app**:  
   Once everything is set up, you can launch the Streamlit app by running the following command:
   ```bash
   streamlit run (filepath)/ev_analysis.py
   ```

5. **Access the dashboard**:
   After running the command, a local URL will be provided in the terminal, something like `http://localhost:8501`. Open that link in your browser to view and interact with the dashboard.

### Project Structure

```
ev-adoption-washington/
│
├── data/                   # Folder containing the data files in pickle format
├── ev_analysis.py          # Main Python file for Streamlit app
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and instructions (this file)
```

## Data Sources

This dashboard leverages the following data:
- **Electric Vehicle Population in Washington State**
- **Washington State General Election Results 2022**
- **Alternative Fuel Stations (Charging Stations) in Washington**
- **Median Household Income by Legislative District**
- **Electric Vehicle Registration Counts by State**

## Acknowledgements

Special thanks to the open data sources and tools that made this analysis possible. This project was built using:
- **Streamlit** for the interactive web app.
- **Plotly** for visualizing data in dynamic, interactive plots.
- **Pandas** and **NumPy** for data manipulation and analysis.

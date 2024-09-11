# **Oversize PV Project**
This repository contains the Python code used to analyze the optimization of the Inverter Loading Ratio (ILR) for utility-scale photovoltaic (PV) systems, specifically for maximizing economic benefits in grid-constrained environments. The study also includes financial modeling (NPV, IRR) and power loss calculations due to inverter clipping.

## **Table of Contents**
- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [File Descriptions](#file-descriptions)
- [License](#license)

## **Project Overview**
This project focuses on optimizing ILR to increase energy output from existing PV systems without needing new grid connections. By using high-resolution solar and meteorological data, the project models energy production, evaluates clipping losses, and performs a financial analysis using Net Present Value (NPV) and Internal Rate of Return (IRR).

### **Key Features:**
- High-resolution (1-minute) energy simulation.
- Clipping analysis for various ILR values.
- Financial performance evaluation (NPV, IRR).
- Integration with Open Meteo API for temperature and wind speed data.
  
## **Data Sources**
- **CAMS**: Solar radiation data for Madrid, Spain.
- **Open Meteo API**: Weather data (temperature, wind speed) used in energy simulations.

## **Project Structure**

```bash
/oversize-pv-project
│
├── /data/                    # Solar radiation and weather data
│   └── 2022_data_madrid.csv   # Sample data file for Madrid, Spain
│
├── /src/                     # Python source code
│   ├── main.py               # Main script that runs the full analysis
│   ├── clipping_calculations.py  # Inverter clipping calculations
│   ├── energy_calculations.py   # Energy production and conversion calculations
│   ├── financial_calculations.py # NPV, IRR financial calculations
│   ├── plots.py               # Script for generating plots
│   └── weather_data.py        # Script for fetching weather data from Open Meteo API
│
├── requirements.txt          # List of required Python packages
├── README.md                 # Overview and project documentation
└── LICENSE                   # License file
```
## **File Descriptions**

### `get_meteo.py`
This script contains the function `get_meteo_data`, which retrieves historical meteorological data (temperature and wind speed) from the Open Meteo API. The function processes the data into a minute-level temporal resolution to match the solar data. It returns a DataFrame with these environmental parameters for each location.

### `solar_data.py`
This script processes solar irradiance data from the Copernicus Atmosphere Monitoring Service (CAMS). It cleans the data and converts it from hourly to minute-level resolution, adjusting for the specific requirements of the photovoltaic (PV) system analysis. The cleaned solar data is used for simulating PV energy generation.

### `pv_system_config.py`
This script defines the configuration of the PV system. It includes the number of inverters, strings per inverter, modules per string, and calculates the DC and AC power for various Inverter Loading Ratio (ILR) levels. The script also initializes the PV modules and inverters used in the analysis.

### `run_model.py`
This script integrates the meteorological data and the solar irradiance data to simulate the power output of the PV system. It uses the pvlib Python library and the Sandia Array Performance Model to calculate the AC power output for different ILR levels, while considering environmental factors such as temperature and irradiance.

### `clipping_analysis.py`
This script analyzes the energy lost due to inverter clipping. It calculates the amount of energy that could not be converted from DC to AC because the generated power exceeds the inverter's capacity. The results are then used to assess the impact of different ILR values on system efficiency.

### `financial_analysis.py`
This script performs the financial analysis of the PV system. It calculates the system costs, including capital expenditure and operational costs, based on real-world data. It also computes financial metrics such as Net Present Value (NPV), Internal Rate of Return (IRR), and NPV-to-Investment Ratio for different ILR levels.

### `plots.py`
This script generates visualizations of the energy production, inverter clipping, and financial results. It includes line and bar plots to illustrate how different ILR values impact the PV system’s performance, energy output, and economic profitability.

### `main.py`
The main entry point for running the complete analysis. This script calls the other modules to execute the full process, from data acquisition to energy and financial analysis. It ties all the steps together, producing final results and visualizations for the PV system's performance across different ILR scenarios.

## License
This project is licensed under the MIT License. See the [LICENSE](notebooks/LICENSE) file for more details.

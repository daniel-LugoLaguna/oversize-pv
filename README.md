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
│   └── 2022_data_madrid.zip   # Sample data file for Madrid, Spain
│
├── /src/
│   ├── main.py                  # Archivo principal que ejecuta todas las funciones
│   ├── financial_calculations.py # Cálculos financieros como NPV y IRR
│   ├── energy_calculations.py    # Cálculos de producción de energía en MW y MWh
│   ├── clipping_calculations.py  # Cálculos de energía perdida por clipping
│   ├── plots.py                 # Generación de gráficos para los resultados
│
├── requirements.txt          # List of required Python packages
├── README.md                 # Overview and project documentation
└── LICENSE                   # License file
```
## **File Descriptions**

### `main.py`: 
  This is the main entry point of the project. It imports the necessary modules for energy and financial calculations, executes the simulation, and generates the relevant plots. It processes different PPA prices (€/MWh) and visualizes the NPV-to-investment ratio, NPV, IRR, and inverter clipping.

### `financial_calculations.py`: 
  Contains functions to calculate the financial performance of the PV system. These include calculating the benefits (NPV and IRR) based on different PPA prices. The function `calculate_benefit` computes the economic benefits, and `calculate_financials` calculates the NPV and IRR for different ILR values.

### `energy_calculations.py`: 
  Handles the simulation of the energy production from the PV system. It defines the PV system using the `pvlib` library and calculates the power output (both AC and DC). This file also converts power (MW) into energy (MWh) and returns the yearly energy produced for each ILR value.

### `clipping_calculations.py`: 
  Defines the function to calculate inverter clipping. This determines how much energy is lost due to oversizing by comparing the DC input power from the solar array with the inverter's maximum AC power capacity. The function generates a DataFrame of clipping results for various ILR values.

### `plots.py`
  Contains functions to generate the plots for visualizing the results. It includes plots for:
    - NPV-to-Investment Ratio vs. ILR (`plot_npv_ratio`)
    - NPV vs. ILR (`plot_npv`)
    - IRR vs. ILR (`plot_irr`)
    - Inverter clipping vs. ILR (`plot_clipping`)

## License
This project is licensed under the MIT License. See the [LICENSE](notebooks/LICENSE) file for more details.

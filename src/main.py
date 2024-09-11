import pandas as pd
import numpy as np
from financial_calculations import calculate_financials, calculate_benefit
from energy_calculations import system_output_energy_mwh, yearly_energy_produced_mwh, df_ILR_cost_euros, df_ILR_energy_mwh
from plots import plot_npv_ratio, plot_npv, plot_irr, plot_clipping
from clipping_calculations import clippingdf_group

# PPA price factors in €/MWh
ppa_prices = [35, 50, 65, 100]  # €/MWh

# Dictionary to store financial results for each PPA factor
financial_results = {}

# Generate benefits and financial calculations for each PPA price
for ppa in ppa_prices:
    df_ILR_cf = calculate_benefit(df_ILR_energy_mwh, ppa)
    financial_results[ppa] = calculate_financials(df_ILR_cf)

# Select the 50 €/MWh PPA factor for plotting
df_fin_profit_ilr = financial_results[50]

# Financial plots
plot_npv_ratio(df_fin_profit_ilr)
plot_npv(df_fin_profit_ilr)
plot_irr(df_fin_profit_ilr)

# Clipping plot
plot_clipping(clippingdf_group)

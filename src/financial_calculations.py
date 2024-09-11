import numpy as np
import numpy_financial as npfin
import pandas as pd

# Calculate financial benefits for each ILR and PPA value
def calculate_benefit(df, factor):
    df_benefit = df.mul(factor)
    df_benefit.insert(loc=0, column='year0', value=-df_ILR_cost_euros['TotalCost'])
    return df_benefit

# Calculate NPV and IRR for each ILR
def calculate_financials(df_benefit):
    npv_ilr = []
    irr_ilr = []
    
    for _, row in df_benefit.iterrows():
        npv_ilr.append(npfin.npv(discountRate, row))
        irr_ilr.append(npfin.irr(row))
    
    df_fin_profit_ilr = pd.DataFrame({
        'NPV': npv_ilr,
        'Initial_invest': df_ILR_cost_euros['TotalCost'],
        'IRR': irr_ilr
    })
    df_fin_profit_ilr['npv/I'] = df_fin_profit_ilr['NPV'] / df_fin_profit_ilr['Initial_invest']
    df_fin_profit_ilr.insert(loc=0, column='ILR_value', value=df_fin_profit_ilr.index.str.split('_').str[1])
    
    return df_fin_profit_ilr

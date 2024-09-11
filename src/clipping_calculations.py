import numpy as np
import pandas as pd

# Function to calculate clipping for each ILR value
def calculate_clipping(P_AC_output_power_inverter_MVA, system_output_power_dc, system_output_power_ac):
    clipping_df = pd.DataFrame(columns=['ILR', 'DC_SolarField_Power_MW', 'AC_power_MW', 'DC_power_MW', 'clipping_power_MW',
                                        'AC_energy_MWh', 'DC_energy_MWh', 'clipping_energy_MWh', 'AC_energy_MWh_ILR_1_0'])
    
    energy_ac_MWh_ilr_1_0 = system_output_power_ac[0]  # Base case for ILR 1.0 (no oversizing)

    for index, (dc_power, ac_power, ilr) in enumerate(zip(system_output_power_dc, system_output_power_ac, ILR_round)):
        clip = pd.DataFrame({
            'ILR': 'ILR_' + str(ilr),
            'DC_SolarField_Power_MW': dc_power,
            'AC_power_MW': ac_power,
            'DC_power_MW': system_output_power_dc[index]
        })
        clip['clipping_power_MW'] = np.where(ac_power >= P_AC_output_power_inverter_MVA,
                                             dc_power - P_AC_output_power_inverter_MVA, 0)
        clip['AC_energy_MWh'] = clip['AC_power_MW'] / 60
        clip['DC_energy_MWh'] = clip['DC_power_MW'] / 60
        clip['clipping_energy_MWh'] = clip['clipping_power_MW'] / 60
        clip['AC_energy_MWh_ILR_1_0'] = energy_ac_MWh_ilr_1_0
        clipping_df = pd.concat([clipping_df, clip])

    return clipping_df

# Calculate clipping group
clippingdf_group = calculate_clipping(P_AC_output_power_inverter_MVA, system_output_power_dc, system_output_power_ac)

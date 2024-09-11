import pvlib
import pandas as pd
import numpy as np
from pvlib.pvsystem import PVSystem
from pvlib.modelchain import ModelChain

# Define the energy calculation for each ILR value
def calculate_energy(solar_weather_df, inverter, module, temperature_parameters, site_location, n_strings, n_inv):
    system_output_power_ac = []
    system_output_power_dc = []
    
    for string in n_strings:
        system = PVSystem(surface_tilt=tilt, surface_azimuth=surface_azimuth, 
                          module_parameters=module, inverter_parameters=inverter,
                          modules_per_string=n_modules_per_strings, strings_per_inverter=string,
                          temperature_model_parameters=temperature_parameters)
        modelchain = ModelChain(system=system, location=site_location, aoi_model='no_loss', spectral_model='no_loss')
        modelchain.run_model(solar_weather_df)
        
        # Append AC and DC power output for each ILR value
        results_df_ac = n_inv * modelchain.results.ac / 1000000  # Convert to MW
        results_df_dc = n_inv * modelchain.results.dc['p_mp'] / 1000000  # Convert to MW
        results_df_ac[results_df_ac < 0] = 0
        results_df_dc[results_df_dc < 0] = 0
        system_output_power_ac.append(results_df_ac)
        system_output_power_dc.append(results_df_dc)
    
    return system_output_power_ac, system_output_power_dc

# Convert power (MW) to energy (MWh)
def convert_power_to_energy(system_output_power_ac):
    system_output_energy_mwh = []
    for power_ac in system_output_power_ac:
        system_output_energy_mwh.append(power_ac / 60)
    
    yearly_energy_produced_mwh = [sum(energy_ilr) for energy_ilr in system_output_energy_mwh]
    return system_output_energy_mwh, yearly_energy_produced_mwh

# Calculate energy
system_output_power_ac, system_output_power_dc = calculate_energy(solar_weather_df, inverter, module, temperature_parameters, site_location, n_strings, n_inv)
system_output_energy_mwh, yearly_energy_produced_mwh = convert_power_to_energy(system_output_power_ac)

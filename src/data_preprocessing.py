import pandas as pd
import numpy as np
import requests
import time

# Function to get meteorological data from Open Meteo API
def get_meteo_data(coord_df, start_date, end_date):
    city = coord_df.apply(tuple, axis=1).to_dict()
    data_list = []
    variable = "temperature_2m,wind_speed_10m"
    
    for city_name, (lat, lon) in city.items():
        url = f'https://archive-api.open-meteo.com/v1/era5?latitude={lat}&longitude={lon}&hourly={variable}&timezone=GMT&start_date={start_date}&end_date={end_date}'
        response = requests.get(url).json()
        df = pd.DataFrame(response['hourly'])
        df['lat'], df['lon'], df['city'] = lat, lon, city_name
        data_list.append(df)
        time.sleep(5)  # Delay to avoid overloading the API
    
    meteo_data = pd.concat(data_list)
    # Repeat hourly data to match the minute resolution
    meteo_data = meteo_data.loc[meteo_data.index.repeat(60)]
    meteo_data.reset_index(drop=True, inplace=True)
    
    # Generate minute-level time index
    date_range = pd.date_range(start=start_date, end=end_date, freq='1min', tz='UTC')
    meteo_data['time'] = np.tile(date_range, len(city))
    
    return meteo_data.set_index('time')

# Function to load and preprocess solar radiation data from the CSV
def load_solar_radiation_data(file_path):
    df = pd.read_csv(file_path, sep=';')
    times = pd.date_range('01-01-2022', periods=60*24*365, freq='1min', tz='UTC')
    df.set_index(times, inplace=True)
    df.rename(columns={'GHI': 'ghi', 'BHI': 'dni', 'DHI': 'dhi'}, inplace=True)
    
    # Convert irradiation from Wh/m2 to W/m2 by multiplying by 60 (minute resolution)
    df['ghi'] *= 60
    df['dni'] *= 60
    df['dhi'] *= 60
    
    return df

# Function to merge meteorological and solar data
def merge_solar_and_meteo_data(coord_df, start_date, end_date, solar_file_path):
    meteo_data = get_meteo_data(coord_df, start_date, end_date)
    solar_data = load_solar_radiation_data(solar_file_path)
    
    # Merge solar and meteorological data
    combined_data = solar_data.merge(meteo_data, left_index=True, right_index=True, how='inner')
    
    # Convert wind speed from km/h to m/s
    combined_data['wind_speed_10m'] *= 1000 / 3600
    
    return combined_data

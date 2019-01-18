# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

city = pd.read_csv('city.csv')
city = city.fillna(city.mean())
globalt = pd.read_csv('global.csv')
globalt = globalt.fillna(city.mean())
city_year = city.iloc[:,0].values
city_temp = city.iloc[:,3].values
global_year = globalt.iloc[46:264:,0].values
global_temp = globalt.iloc[46:264:,1].values

city_average_7_years = np.convolve(city_temp, np.ones((7,))/7, mode='valid')
global_average_7_years = np.convolve(global_temp, np.ones((7,))/7, mode='valid')
temp_year = city_year[0:212]
plt.plot(temp_year,city_average_7_years,label='Pune')
plt.plot(temp_year,global_average_7_years,label='Global')
plt.title('Global, Pune Temperatures over the Years')
plt.xlabel('Years')
plt.ylabel('Temp (deg C)')
plt.legend()
plt.show()

corrcoef = np.corrcoef(city_temp,global_temp)
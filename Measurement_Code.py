#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Measures Temperature, Humidity, Pressure
# BME280 - Adafruit
# Write the data to a file - a time column, temperature, humidity, pressure
# - look up Adafruit CircuitPython BME280 module
# - update code to use that module

import csv
import time
import math
from Adafruit_BME280 import *

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode = BME280_OSAMPLE_8)

times = []
temperatures = []
pressures = []
humidities = []


start_time = time.time()
run_time = 10
stop_time = start_time + run_time
current_time = time.time()
while current_time < stop_time:
    current_time = time.time()
    temp = bme.readTemperature()
    pressure = bme.readPressure()
    humidity = bme.readHumidity()
    current_time = time.time()
    print(temp)
    print(pressure)
    print(humidity)
    times.append(current_time)
    temperatures.append(temp)
    pressures.append(pressure)
    humidities.append(humidity)
    time.sleep(1)

data = [times, temperatures, pressures, humidities]
    
with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for value in data:
        word = value
        for num in word:
            writer.writerow([num])

import pandas as pd

df = pd.DataFrame({'time': times, 'temperatures': temperatures, 'pressures': pressures, 'humidities': humidities})
print(df)
df.to_csv('test.csv', index=False, header=True)
    
##with open('test.csv', 'w', newline='') as f:
    ##writer = csv.writer(f)
    ##writer.writerows(data)


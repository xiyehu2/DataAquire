# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 08:09:20 2018

@author: 14625
"""
import datetime
import numpy as np
import matplotlib.pyplot as plt

data=np.genfromtxt("D:\\Physics398DLP\\8_hour_test_run.txt", delimiter = ',', skip_header = 4, skip_footer = 1)


count = int(len(data)/2)

time_hour = np.zeros(count)
time_min = np.zeros(count)
time_sec = np.zeros(count)
time_ms = np.zeros(count)
temperature = np.zeros(count)
pressure = np.zeros(count)
humidity = np.zeros(count)
altitude = np.zeros(count)
seconds = np.zeros(count)

#print(data)



for n in range(0,len(data)):
    if n%2 == 0:
        time_hour[int(n/2)] = (data[n,0])
        time_min[int(n/2)] = (data[n,1])
        time_sec[int(n/2)] = (data[n,2])
        time_ms[int(n/2)] = (data[n,3])
    else:
        temperature[int((n-1)/2)] = (data[n,0])
        pressure[int((n-1)/2)] = (data[n,1])
        humidity[int((n-1)/2)] = (data[n,2])
        altitude[int((n-1)/2)] = (data[n,3])
        

t0 = time_hour[0]*3600 + time_min[0]*60 + time_sec[0] + time_ms[0]*0.001
init_time = np.linspace(t0,t0,count)
seconds = time_hour*3600 + time_min*60 + time_sec + time_ms*0.001 - init_time

        

plt.plot(seconds,temperature, 'y')
plt.title('Temperature(°C) vs Time')
plt.xlabel('t')
plt.ylabel('T')
plt.show()

plt.plot(seconds,pressure, 'm')
plt.title('Pressure(hPa) vs Time')
plt.xlabel('t')
plt.ylabel('P')
plt.show()

plt.plot(seconds,humidity, 'c')
plt.title('Humidity(%) vs Time')
plt.xlabel('t')
plt.ylabel('H')
plt.show()

#plt.plot(seconds,altitude, 'k')
#plt.title('Altitude(m) vs Time')
#plt.xlabel('t')
#plt.ylabel('m')
#plt.show()





# syncronize clocks different devices
# measure settling time for humidity, etc.
# anamometer
# pcb and bredboard ready
# case design

# check the heater on bme
# test IR sensor
# still anamometer
# still settling time
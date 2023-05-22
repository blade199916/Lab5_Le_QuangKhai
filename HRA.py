
"""
Created on Sun Mar 26 15:04:23 2023

@author: Quang Khai Le
"""

#heart rate
#import packages

import heartpy as hp
import matplotlib.pyplot as plt

#time_between_points = 
#data
data = hp.get_data('HB2_Output_mono.csv')
#data = hp.get_data('data.csv')

#plot figures
plt.figure(figsize=(8,3))
plt.plot(data)
plt.show()

#run analysis
sample_rate = 18467.05556  #sample raate 332407 as the last value/18 =18467.05556
#wd = working data-> stores temporatry values
#m = measures -> stores computed measures
wd, m = hp.process(data, sample_rate)

#visualise in plot of custom size
plt.figure(figsize=(200,10))
hp.plotter(wd, m)  #plots working data and measures 

#display computed measures
for measure in m.keys():
    print('%s: %f' %(measure, m[measure])) #print keys
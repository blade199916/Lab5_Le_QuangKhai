# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:04:13 2023

@author: Quang Khai Le
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 12:54:41 2023

@author: Fesehaye Habte
"""

import sys, os, os.path
from scipy.io import wavfile
import pandas as pd

print("start")
input_filename = "HB2.wav"
if input_filename [-3:] != 'wav':
    print('WARNING!! Input File format should be *.wav')
    sys.exit()
    
print("read files")
samrate, data = wavfile.read(str('./wavfile/' + input_filename))
print('Load is Done! \n')

wavData = pd.DataFrame(data)

print("if statements")
if len(wavData.columns) == 2:
    print('Stereo .wav file\n')
    wavData.columns = ['R', 'L']
    stereo_R = pd.DataFrame(wavData['R'])
    stereo_L = pd.DataFrame(wavData['L'])
    print('Saving...\n')
    stereo_R.to_csv(str(input_filename[:-4] + "_Output_stereo_R.csv"))
    stereo_L.to_csv(str(input_filename[:-4] + "_Output_stereo_L.csv"))

    # wavData.to_csv("Output_stereo_RL.csv", mode='w')]
    print('Save is done' + str(input_filename[:-4]) + '_Output_stereo_R.csv')
    print('Save is done' + str(input_filename[:-4]) + '_Output_multi_channel.csv')

elif len(wavData.columns) == 1:
    print('Mono .wav file\n')
    wavData.columns = ['M']
    wavData.to_csv(str(input_filename[:-4] + "_Output_mono.csv"), mode='w')
    print('Save is done' + str(input_filename[:-4]) + '_Output_mono.csv')
else:
    print('Multi channel .wav file\n')
    print('number of channel: ' + len(wavData.columns) + '\n')
    wavData.to_csv(str(input_filename [:-4] + "Output_multi_channel.csv"))
    print('Save is done' + str(input_filename[:-4])+ 'Output_multi_channel.csv')

import sklearn as sk
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
import sklearn.linear_model as lr
import stockdata

#stockdata.acquire()
df = pd.read_csv('s&p500.csv')
symbol = df['symbol'].values
volume = df['volume'].values
flag = 0
flag_list = [flag]
for i in range(1,len(symbol)-2):
    if symbol[i]!=symbol[i+1]:
        flag_list.append(i)
        flag_list.append(i+1)
flag_list.append(len(symbol)-1)
flag_list = np.array(flag_list).reshape(int(len(flag_list)/2),2)
average_volume = [np.average(volume[(flag_list[0][0]):(flag_list[0][1]+1)])]
for i in range(1,len(flag_list)-1):
    average_volume.append(np.average(volume[(flag_list[i][0]):(flag_list[i][1]+1)]))
print(average_volume)
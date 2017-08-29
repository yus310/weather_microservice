import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
%matplotlib inline

username='yus310'
password='123'

# Request forecast for  New Dehli
lat = '28.6139'
lon = '77.2090'
line='<a class="vglnk" href="https://'+username+':'+password+'@twcservice.mybluemix.net/api/weather/v1/geocode/'+lat+'/'+lon+'/forecast/intraday/10day.json?&units=m" rel="nofollow"><span>https</span><span>://'+</span><span>username</span><span>+':'+</span><span>password</span><span>+'@</span><span>twcservice</span><span>.</span><span>mybluemix</span><span>.</span><span>net</span><span>/</span><span>api</span><span>/</span><span>weather</span><span>/</span><span>v1</span><span>/</span><span>geocode</span><span>/'+</span><span>lat</span><span>+'/'+</span><span>lon</span><span>+'/</span><span>forecast</span><span>/</span><span>intraday</span><span>/</span><span>10day</span><span>.</span><span>json</span><span>?&</span><span>units</span><span>=</span><span>m</span></a>'
r=requests.get(line)
weather = json.loads(r.text)

print json.dumps(weather,indent=1)

df = pd.DataFrame.from_dict(weather['forecasts'][0],orient='index').transpose()
for forecast in weather['forecasts'][1:]:
    df = pd.concat([df, pd.DataFrame.from_dict(forecast,orient='index').transpose()])

time = np.array(df['fcst_valid_local'])
for row in range(len(time)):
    time[row] = datetime.strptime(time[row], '%Y-%m-%dT%H:%M:%S+0100')

df = df.set_index(time)

list(df)

df['rain'] = df['pop'].as_matrix()
df=df.drop('pop',1)

tmean = pd.rolling_mean(df['temp'], window=4, center=True)
rhmean = pd.rolling_mean(df['rh'], window=4, center=True)
cldsmean = pd.rolling_mean(df['clds'], window=4, center=True)
wspdmean = pd.rolling_mean(df['wspd'], window=4, center=True)
rainmean = pd.rolling_mean(df['rain'], window=4, center=True)

matplotlib.style.use('bmh')

fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(8, 10))

df['temp'].plot(ax=axes[0], color='dodgerblue',sharex=True)
tmean.plot(ax=axes[0], kind='line',color='darkorchid', sharex=True)
axes[0].set_ylabel('temperature [$^o$C]')

df['rain'].plot(ax=axes[1], color='dodgerblue',sharex=True)
axes[1].set_ylabel('chance of rain [%]')

df['rh'].plot(ax=axes[2], color='dodgerblue',sharex=True)
rhmean.plot(ax=axes[2], kind='line',color='darkorchid', sharex=True)
axes[2].set_ylabel('humidity [%]')

df['clds'].plot(ax=axes[3], color='dodgerblue',sharex=True)
cldsmean.plot(ax=axes[3], kind='line',color='darkorchid', sharex=True)
axes[3].set_ylabel('clouds [%]')

df['wspd'].plot(ax=axes[4], color='dodgerblue',sharex=False)
wspdmean.plot(ax=axes[4], kind='line',color='darkorchid', sharex=True)
axes[4].set_ylabel('wind [m s$^{-1}$]')
output_6_2



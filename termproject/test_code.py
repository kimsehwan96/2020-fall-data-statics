import numpy as np
import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./references/iot_telemetry_data.csv',engine='python')
#전처리 
# 1. 디바이스 이름을 덜 복잡한 이름으로 변경
# 2. timstamp를 datatime으로 변경.

df.replace(['00:0f:00:70:91:0a', '1c:bf:ce:15:ec:4d', 'b8:27:eb:bf:9d:51'], [1, 2, 3], inplace=True)
df['time_stamp'] = pd.to_datetime(df['ts'],unit='s')
df.drop(columns=['ts'], inplace=True)

df_1 = df[df.device == 1]
df_2 = df[df.device == 2]
df_3 = df[df.device == 3]

print(df_1)
print(df_2)
print(df_3)

import matplotlib.dates as mdates

plt.style.use('dark_background')

plt.figure(figsize=(20,10))
ax1 = sns.lineplot(df_1.time_stamp, df_1.co, color = 'yellow', label = 'device 1')
ax2 = sns.lineplot(df_2.time_stamp, df_2.co, color = 'red', label = 'device 2')
ax3 = sns.lineplot(df_3.time_stamp, df_3.co, color = 'green', label = 'device 3')
ax3.xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.ylabel('carbon monoxide (ppm)', fontsize = 18)
plt.xlabel('')
plt.legend(fontsize = 18)
plt.show()

plt.figure(figsize=(20,10))
ax1 = sns.lineplot(df_1.time_stamp, df_1.humidity, color = 'yellow', label = 'device 1')
ax2 = sns.lineplot(df_2.time_stamp, df_2.humidity, color = 'red', label = 'device 2')
ax3 = sns.lineplot(df_3.time_stamp, df_3.humidity, color = 'green', label = 'device 3')
ax3.xaxis.set_major_locator(mdates.DayLocator(interval=1))
vals = ax3.get_yticks()
ax3.set_yticklabels(['{:,.0%}'.format(x) for x in vals])
plt.ylabel('humidity', fontsize = 18)
plt.legend(fontsize = 18)
plt.xlabel('')
plt.show()

plt.figure(figsize=(20,10))
ax1 = sns.lineplot(df_1.time_stamp, df_1.lpg, color = 'yellow', label = 'device 1')
ax2 = sns.lineplot(df_2.time_stamp, df_2.lpg, color = 'red', label = 'device 2')
ax3 = sns.lineplot(df_3.time_stamp, df_3.lpg, color = 'green', label = 'device 3')
ax3.xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.ylabel('liquid petroleum gas (ppm)', fontsize = 18)
plt.xlabel('')
plt.legend(fontsize = 18)
plt.show()

plt.figure(figsize=(20,10))
ax1 = sns.lineplot(df_1.time_stamp, df_1.smoke, color = 'yellow', label = 'device 1')
ax2 = sns.lineplot(df_2.time_stamp, df_2.smoke, color = 'red', label = 'device 2')
ax3 = sns.lineplot(df_3.time_stamp, df_3.smoke, color = 'green', label = 'device 3')
ax3.xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.ylabel('smoke (ppm)', fontsize = 18)
plt.xlabel('')
plt.legend(fontsize = 18)
plt.show()

plt.figure(figsize=(20,10))
ax1 = sns.lineplot(df_1.time_stamp, df_1.temp, color = 'yellow', label = 'device 1')
ax2 = sns.lineplot(df_2.time_stamp, df_2.temp, color = 'red', label = 'device 2')
ax3 = sns.lineplot(df_3.time_stamp, df_3.temp, color = 'green', label = 'device 3')
ax3.xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.ylabel('temperature (fahrenheit)', fontsize = 18)
plt.xlabel('')
plt.legend(fontsize = 18)
plt.show()
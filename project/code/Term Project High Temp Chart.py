import pandas as pd

import matplotlib.pyplot as plt

weather = pd.read_csv("C:\Python27\Scripts\Wunderground_Data.csv")
weathernew = weather[['Date', 'PWS', 'Temperature']]

plt.figure(figsize=(20,10))

plt.ylim(65, 85)
plt.bar(weathernew['PWS'], weathernew['Temperature'])

plt.xlabel('Weather Stations')
plt.ylabel('Temperature (F)')
plt.title('Weekly Record Temperatures')
plt.legend()

plt.show()
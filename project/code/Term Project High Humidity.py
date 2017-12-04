import pandas as pd

import matplotlib.pyplot as plt

weather = pd.read_csv("C:\Python27\Scripts\Wunderground_Data.csv")
weathernew = weather[['Date', 'PWS', 'Humidity']]

plt.figure(figsize=(20,15))

plt.ylim(.5, 1.0)
plt.bar(weathernew['PWS'], weathernew['Humidity'])

plt.xlabel('Weather Stations')
plt.ylabel('Humidity (%)')
plt.title('Weekly Record Humidity')
plt.legend()

plt.show()
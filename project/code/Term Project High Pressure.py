import pandas as pd

import matplotlib.pyplot as plt

weather = pd.read_csv("C:\Python27\Scripts\Wunderground_Data.csv")
weathernew = weather[['Date', 'PWS', 'Pressure']]

plt.figure(figsize=(20,15))

plt.ylim(28, 31)
plt.bar(weathernew['PWS'], weathernew['Pressure'])

plt.xlabel('PWS')
plt.ylabel('Pressure')
plt.title('Weekly Record Pressure')
plt.legend()

plt.show()
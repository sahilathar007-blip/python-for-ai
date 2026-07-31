# Date and time
import datetime

today = datetime.date.today()  # noqa: DTZ011
print(today)  # 2024-01-15


import math

result = math.sqrt(16)
print(result)  # 4.0

# Date and time
import datetime

today = datetime.date.today()  # noqa: DTZ011
print(today)  # 2024-01-15

# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])
print(number)  # Random integer between 1 and 10
print(choice)  # Random choice from the list

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=28.84&longitude=78.77&daily=temperature_2m_max,temperature_2m_min&timezone=auto"

response = requests.get(url)

data = response.json()

daily_data = data["daily"]

print(daily_data)

import pandas as pd
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=28.84&longitude=78.77&daily=temperature_2m_max,temperature_2m_min&timezone=auto"

response = requests.get(url)

data = response.json()
 
df = pd.DataFrame({
    "date": daily_data["time"],
    "max_temp": daily_data["temperature_2m_max"],
    "min_temp": daily_data["temperature_2m_min"]
})

print(df)
print(df.head())
print(df.describe())

import os
 
import matplotlib.pyplot as plt
import pandas as pd
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=28.84&longitude=78.77&daily=temperature_2m_max,temperature_2m_min&timezone=auto"

response = requests.get(url)
data = response.json()

daily_data = data['daily']
# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)
#--------------------------------

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()
print(df.head())
print(df.describe())
print(df['max_temp'].mean())
print(df['min_temp'].mean())

#-------------------------------


# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/paris_weather.csv', index=False)
print("Data saved to data/paris_weather.csv")
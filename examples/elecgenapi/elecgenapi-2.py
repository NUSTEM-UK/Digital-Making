"""Output current UK electricity supply generation mix.

Simple example of parsing a JSON API source. See
'example.json' for what the response looks like.

Uses the requests library, which automatically parses JSON data.

Based on example code from NationalGrid: 
https://carbon-intensity.github.io/api-definitions/?python#generation

Pie chart code from matplotlib docs:
https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html
"""

import requests
import matplotlib.pyplot as plt

headers = {
    'Accept': 'application/json'
}

r = requests.get('https://api.carbonintensity.org.uk/generation', params={}, headers=headers)

mix = r.json()

# Make empty lists in which we'll hold the data
fueltype = []
percentage = []

for fuel in mix['data']['generationmix']:
    # Add the fuel type and percentage to the respective lists
    fueltype.append(fuel['fuel'])
    percentage.append(fuel['perc'])

# Set up a chart
fix1, ax1 = plt.subplots()
# Plot a pie chart of the percentage data, using fueltype as labels.
ax1.pie(percentage, labels=fueltype, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle

# Present the pie chart. Close the window to exit the program
plt.show()
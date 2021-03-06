"""Query the 'People in Space' API.

Based on code from Raspberry Pi project:
https://projects.raspberrypi.org/en/projects/people-in-space-indicator

Note that the data source is updated manually!
http://open-notify.org/Open-Notify-API/People-In-Space/
"""

import requests

r = requests.get('http://api.open-notify.org/astros.json')

# Parse the response as JSON - example data in example.json
data = r.json()

# Iterate over the people element of the returned JSON
for person in data['people']:
    print(person['name'])

print("-----")
print("Total people in space: ", data['number'])

# Maybe use something physical to represent the number of people? 
# Like a set of LEDs as a bar graph LEDBarGraph from GPIOzero:
# https://gpiozero.readthedocs.io/en/stable/api_boards.html#ledbargraph
# ...or a multi-segment display in HAT.
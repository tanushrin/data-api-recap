# pylint: disable=missing-docstring,invalid-name

import requests

url = "https://weather.lewagon.com/geo/1.0/direct?q=Barcelona"

print(requests.get(url))
#-> Prints <Response [200]> i.e. HTTP OK Status

response = requests.get(url).json()
#print(response[0]) #prints dict
city = response[0]
print(f"{city['name']}: ({city['lat']}, {city['lon']})")
#Prints Barcelona: (41.3828939, 2.1774322)

# pylint: disable=missing-module-docstring

import sys
#import urllib.parse
import requests



'''
Is this a REST API? - Yes
Does it serve JSON? - Yes
Does this API require authentication?
(do I need to sign up to get an API key?  - Yes
Do I need to pay?)
What is the base URI? - https://api.openweathermap.org/
Which endpoints can I call? What data does it return?
- 3 endpoints:
    1) Current weather and forecasts
    2) Weather data for any timestamp for 40+ years historical archive and 4 days ahead forecast
    3) Daily aggregation of weather data for 40+ years archive and 1.5 years ahead forecast


'''
BASE_URI = "https://weather.lewagon.com"
#Example: https://weather.lewagon.com/geo/1.0/direct?q=Barcelona


def search_city(query):
    '''
    Look for a given city. If multiple options are returned, have the user choose between them.
    Return one city (or None)
    '''
    url = "https://weather.lewagon.com/geo/1.0/direct?q="+query
    response = requests.get(url).json()

    if len(response) !=0:
        city = response[0]
        return city
    return None

def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    url = "https://weather.lewagon.com/data/2.5/forecast?lat="+str(lat)+"&lon="+str(lon)
    response = requests.get(url).json()

    if len(response) !=0:
        each_dict = response.get("list")
        new_lst = []

        for index, record in enumerate(each_dict):
            if (index%9) == 0:
                new_lst.append(record)
                return new_lst
    return None

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    weather_forecast(city['lat'], city['lon'])

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)

#import the requests library
import requests

#include the access key and the query
params = {
  'access_key': 'YOUR_ACCESS_KEY',
  'query': 'New York'
}

#Send a GET request to the Weatherstack API
api_result = requests.get('https://www.metaweather.com/api/', params)

#store the response data in JSON format
api_response = api_result.json()

#print the current temperature of the specified location, which is Chicago,IL USA

print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))

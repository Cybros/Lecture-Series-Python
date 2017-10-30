## Get latitude and longitude from google maps for any address
## register fro google maps api and get keys
import requests

address = "RMZ Infinity , Bangalore"
api_key = "google maps api key"
api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
api_response_dict = api_response.json()

if api_response_dict['status'] == 'OK':
    latitude = api_response_dict['results'][0]['geometry']['location']['lat']
    longitude = api_response_dict['results'][0]['geometry']['location']['lng']
    print 'Latitude:', latitude
    print 'Longitude:', longitude

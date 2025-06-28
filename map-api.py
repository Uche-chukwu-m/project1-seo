import requests
import os
import googlemaps
from datetime import datetime

BASE_URL = "https://maps.googleapis.com/maps/api/directions/"
api_key = os.getenv("MAPS_API_KEY")
gmaps = googlemaps.Client(key=api_key)

from_where = input("Enter your address: ")
to_where = input("Enter where you want to go: ")
time = datetime.now()

directions_result = gmaps.directions(from_where, to_where, mode='transit', departure_time=time)
print(directions_result[0].json())
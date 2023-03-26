#!/usr/bin/env python3

import requests

response = requests.get("https://opendomesday.org/api/county/Derbyshire/places/ids/")
places = response.json()

print(places)

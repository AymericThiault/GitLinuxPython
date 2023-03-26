#!/usr/bin/env python3

import requests

def get_manor_ids(place_id):
    """
    Returns the list of manor ids for a given place id.
    """
    url = f"https://opendomesday.org/api/places/{place_id}/manors/"
    response = requests.get(url)
    data = response.json()
    manor_ids = [manor["id"] for manor in data["results"]]
    return manor_ids

if __name__ == '__main__':
    place_id = "20086"
    manor_ids = get_manor_ids(place_id)
    print(manor_ids)

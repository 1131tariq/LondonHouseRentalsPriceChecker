import requests
import json

API = "AIzaSyB1HxFeplrmRTXu19qr4EL934J7Mi6eszw"
URL = "https://maps.googleapis.com/maps/api/directions/json"
Westminister = "University of Westminster - Cavendish Campus, University of Westminster Cavendish Campus, New Cavendish Street, London, UK"
City = "City, University of London, Northampton Square, London, UK"


def distance_city(origin):
    params = {
        "origin": origin,
        "destination": City,
        "mode": "transit",
        "fields": "duration",
        "key": API
    }
    response = requests.get(url=URL, params=params)
    data = response.json()
    # data = json.dumps(data, indent=1, sort_keys=True)
    try:
        time_needed = data["routes"][0]["legs"][0]["duration"]["value"]
    except IndexError:
        time_needed = None
        if time_needed is None:
            transit_time = 1 / 60
    else:
        transit_time = int(time_needed) / 60
    finally:
        return transit_time


def distance_wst(origin):
    params = {
        "origin": origin,
        "destination": Westminister,
        "mode": "transit",
        "fields": "duration",
        "key": API
    }
    response = requests.get(url=URL, params=params)
    data = response.json()
    # data = json.dumps(data, indent=1, sort_keys=True)
    try:
        time_needed = data["routes"][0]["legs"][0]["duration"]["value"]
    except IndexError:
        time_needed = None
        if time_needed is None:
            transit_time = 1 / 60
    else:
        transit_time = int(time_needed) / 60
    finally:
        return transit_time

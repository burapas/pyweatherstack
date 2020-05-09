import json
import logging

import requests

def route(func):
    def _route(self, *args, **kwargs):
        print("running..")
        try:
            params = func(self, *args, **kwargs)
            url = f"{self.protocol}{self.base_url}/{func.__name__}"
            print(url)
            response = requests.get(url, params=params)
            print(response.url)
            if response.ok:
                return json.loads(response.text)
            else:
                raise Exception(f"Received status code: {response.status_code}")
        except Exception as e:
            logging.exception(e)
    return _route

def authentication(func):
    def _authentication(self, *args, **kwargs):
        if self.access_key is not None:
            return func(self, *args, **kwargs)
        else:
            raise Exception("No ACCESS KEY")
    return _authentication

class WeatherStack:
    def __init__(self, access_key):
        self.base_url = "api.weatherstack.com"
        self.protocol = "http://"
        self.access_key = access_key

    @authentication
    @route
    def current(self, query):
        return {
            "access_key": self.access_key,
            "query": query,
        }

    @authentication
    @route
    def historical(self, query, start_date, end_date,
                   hourly=1, interval=3,  units="m"):
        return {
            "access_key": self.access_key,
            "query": query,
            "historical_date_start": start_date,
            "historical_date_end": end_date,
            "hourly": hourly,
            "interval": interval,
            "units": units,
        }
    
    @authentication
    @route
    def forecast(self, query):
        return {
            "access_key": self.access_key,
            "query": query,
        }
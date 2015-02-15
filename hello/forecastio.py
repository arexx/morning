import requests

from .secrets import FORECAST_IO as SECRET

FORECAST_IO_API_ENDPOINT = "https://api.forecast.io/forecast/"

def get_weather():
	r = requests.get("%s%s/%s" % (FORECAST_IO_API_ENDPOINT, SECRET.API_KEY, SECRET.LOCATION))
	return r.text

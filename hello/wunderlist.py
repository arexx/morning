import requests

from .secrets import WUNDERLIST as SECRET

TASKS_API_ENDPOINT = "https://a.wunderlist.com/api/v1/tasks"

def get_list():
	r = requests.get(
			TASKS_API_ENDPOINT,
			params={
				"list_id": SECRET.LIST_ID,
				"completed": "false",
			},
			headers={
				"X-Access-Token": SECRET.ACCESS_TOKEN,
				"X-Client-Id": SECRET.CLIENT_ID,
			},
		)
	return r.json()

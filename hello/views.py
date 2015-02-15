from django.shortcuts import render
from django.http import HttpResponse

import datetime

from .memo import memo
from .wunderlist import get_list
from .forecastio import get_weather
from .mta import get_mta_html

# Create your views here.
def index(request):
    tasks = memo("WLA", get_list)

    for task in tasks:
    	if 'due_date' in task:
	    	task['time_to_go'] = datetime.datetime.strptime(task['due_date'], "%Y-%m-%d") - datetime.datetime.today()

    return render(request, 'morning.html', {
        "tasks": tasks,
    })

def forecast(request):
	weather_data = get_weather()
	return HttpResponse(weather_data, content_type="application/json")

def mta(request):
	html = get_mta_html()
	return HttpResponse(html)

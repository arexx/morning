from django.shortcuts import render
from django.http import HttpResponse

from .memo import memo
from .wunderlist import get_list
from .forecastio import get_weather

# Create your views here.
def index(request):
    tasks = memo("WLA", get_list)

    return render(request, 'morning.html', {
        "tasks": tasks,
    })

def forecast(request):
	weather_data = get_weather()
	return HttpResponse(weather_data, content_type="application/json")
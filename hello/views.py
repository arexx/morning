from django.shortcuts import render

from .memo import memo
from .wunderlist import get_list

# Create your views here.
def index(request):
    tasks = memo("WLA", get_list)

    return render(request, 'morning.html', {
        "tasks": tasks,
    })


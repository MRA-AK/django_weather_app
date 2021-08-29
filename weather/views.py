from django.http import request
from django.shortcuts import render

from .scrape import scrape_weather



def index(request):
    result = None
    if 'city' in request.GET:
        city = request.GET.get('city')
        result = scrape_weather(city)

    return render(request, 'weather/index.html', {'result': result})
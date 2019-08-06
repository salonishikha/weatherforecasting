# Create your views here.
from django.shortcuts import render

from WebApp.models import Weather


def WeatherView(request):
    ...
    query_results = Weather.objects.all()
    ...
    return render(request, 'datalist.html',
                  {"query_results": query_results})
    #return a response to your template and add query_results to the context
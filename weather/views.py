from typing import Type
from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm

try:
    def index(request):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8cca99374aebcbb9839c3f9feef40c37'
        form = CityForm()
        cities = City.objects.all()

        if request.method == "POST":
            form = CityForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')

        """
		I tried to build the delete function but for some reason it was never working
		but i didn't want the db to store more than 10 city names so i use the the code right below
		"""

        if len(cities) >= 10:
            cities.last().delete()

        try:
            weather_data = []

            for city in cities:
                r = requests.get(url.format(city)).json()

                city_weather = {
                    'country': r['sys']['country'],
                    'city': city.name,
                    'temperature': r['main']['temp'],
                    'description': r['weather'][0]['description'],
                    'icon': r['weather'][0]['icon'],
                    'wind': r['wind']['speed'],
                    'humidity': r['main']['humidity']
                }
                weather_data.append(city_weather)
        except Exception as KeyError:
            cities.first().delete()
            if len(cities) <= 0:
                City.objects.create(name="Accra")

        count = len(cities)

        context = {
            'count': count,
            'city': cities,
            'weather_data': weather_data,
            'form': form
        }

        return render(request, 'weather/index.html', context)
except Exception as a:
    pass

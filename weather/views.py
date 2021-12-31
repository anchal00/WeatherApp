from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city_name = request.POST['city']
        data_url = 'http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=c7c2fc443c3686e279dde0bd32c5a950'
        weather_data = urllib.request.urlopen(data_url).read()
        weather_json_data = json.loads(weather_data)

        if (weather_json_data['cod'] == '404'):
            data = {}
        else:
            data = {
                'city':city_name,
                'country_code':str(weather_json_data['sys']['country']),
                'coordinate':str(weather_json_data['coord']['lon']) + ' ' + str(weather_json_data['coord']['lat']),
                'temp': str(weather_json_data['main']['temp']) +'K',
                'pressure': str(weather_json_data['main']['pressure']),
                'humidity': str(weather_json_data['main']['humidity'])
            }
    else:
        data = {
        }
    return render(request, 'index.html',context = data)
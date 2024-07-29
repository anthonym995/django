from django.shortcuts import render
import requests


def weather(request):
    data = None
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            api_key = '11f8cf82b2add5269d033f38c8d65b00'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
            else:
                data = {'error': "City not found"}
        else:
            data = {'error': "Enter valid city"}

    return render(request, 'weather.html', {'data': data})

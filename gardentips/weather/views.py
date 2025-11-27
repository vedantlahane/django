from django.shortcuts import render
from datetime import datetime, timedelta
import random

def generate_mock_weather():
    conditions = ['Sunny', 'Cloudy', 'Rainy', 'Stormy', 'Windy']
    forecast = []
    today = datetime.today()
    for i in range(5):  # next 5 days
        day = today + timedelta(days=i)
        forecast.append({
            'date': day.strftime('%Y-%m-%d'),
            'temperature': random.randint(18, 35),
            'condition': random.choice(conditions)
        })
    return forecast

def weather_dashboard(request):
    forecast = generate_mock_weather()
    current = forecast[0]
    return render(request, 'weather_dashboard.html', {'forecast': forecast, 'current': current})

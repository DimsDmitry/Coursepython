result = {
            'coord': {'lon': 35.8931, 'lat': 56.8619},
            'weather': [{'id': 800, 'main': 'Clear',
                       'description': 'clear sky', 'icon': '01d'}],
            'base': 'stations',
            'main':
              {'temp': 275.42, 'feels_like': 271.12, 'temp_min': 275.42,
               'temp_max': 275.42, 'pressure': 1017, 'humidity': 80,
               'sea_level': 1017, 'grnd_level': 998},
              'visibility': 10000, 'wind': {'speed': 4.92, 'deg': 219, 'gust': 12.84},
              'clouds': {'all': 9},
              'dt': 1766227975,
              'sys': {'country': 'RU', 'sunrise': 1766211099, 'sunset': 1766235380},
              'timezone': 10800, 'id': 480060, 'name': "Tver'", 'cod': 200
}

print(result['main']['temp'])
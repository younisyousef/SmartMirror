import urllib.request
import json
import time


class Weather:
    def __init__(self, lat = 37.6547, lon = -122.4077):
        secret_key = 'f7866e59a68f8848e213a243c75e339f'
        self._url = f"https://api.darksky.net/forecast/{secret_key}/{lat},{lon}"
        self._time = time.time()
        self._weather_dict = None
        self._load_json()
        
            
    
    def _load_json(self):
        try:
            data = urllib.request.urlopen(self._url)
            self._weather_dict = json.load(data)
        except (Exception):
            time.sleep(5)
            self._load_json()
            

    def _updateData(self):
        if (time.time() - self._time >= 120):
            self._load_json()
            self._time = time.time()
    
    def getCurrentTemp(self):
        self._updateData()
        return self._weather_dict['currently']['temperature']
    
    
    def getWeeklyMax(self):
        self._updateData()
        return [temp['temperatureHigh'] for temp in self._weather_dict['daily']['data']]
    
    def getWeeklyMin(self):
        self._updateData()
        return [temp['temperatureLow'] for temp in self._weather_dict['daily']['data']]
    
    def getCurrentIcon(self):
        self._updateData()
        return self._weather_dict['currently']['icon']
    
    def getWeekIcons(self):
        self._updateData()
        return [temp['icon'] for temp in self._weather_dict['daily']['data']]
    

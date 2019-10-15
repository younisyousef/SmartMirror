import urllib.request
import json
import time

class News:
    def __init__(self):
        api_key = '6f5d3255cbe44f48b32c9d3bbf58554d'
        self._url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        self._time = time.time()
        self._news_dict = None
        self._load_json()
        
    def _load_json(self):
        try:
            data = urllib.request.urlopen(self._url)
            self._news_dict = json.load(data)
        except Exception as e:
            print(e)
            time.sleep(5)
            self._load_json()
            
    def _updateData(self):
        if (time.time() - self._time >= 10):
            print("ok")
            self._load_json()
            self._time = time.time()
    
    def topFiveHeadlines(self):
        self._updateData()
        return [articles['title'] for articles in self._news_dict['articles'][0:5]]

        

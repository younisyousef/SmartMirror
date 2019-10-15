import requests
url = "http://www.forbes.com/forbesapi/thought/uri.json?enrich=true&query=1&relatedlimit=20"
response = requests.get(url)
data = response.json()

def getDailyQuote():
    return (data['thought']['quote'].strip(), "\n-" + data['thought']['thoughtAuthor']['name'])


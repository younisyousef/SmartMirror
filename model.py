import weather
import news
import quotes
import time
from datetime import date
from PIL.ImageTk import PhotoImage, Image



weather_obj = weather.Weather()
news_obj = news.News()
months = ["January", "February", "March", "April", "May", "June", "July",\
                "August", "September", "October", "November", "December"]
    
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",\
                "Saturday", "Sunday"]

large_icons = {"cloudy": Image.open("bigcloudy.png"), "clear-night": Image.open("bignight.png"), "foggy": Image.open('bigcloudy.png')\
               , "partly-cloudy-night": Image.open("bignightcloudy.png"), "partly-cloudy-day": Image.open("bigpartlycloudy.png"),\
               "rain": Image.open("bigrainy.png"), "clear-day": Image.open("bigsun.png"), "thunderstorm": Image.open("bigstorm.png")}

small_icons = {"cloudy": Image.open("cloudy.png"), "clear-night": Image.open("night.png"), "foggy": Image.open('cloudy.png')\
               , "partly-cloudy-night": Image.open("nightcloudy.png"), "partly-cloudy-day": Image.open("partlycloudy.png"),\
               "rain": Image.open("rain.png"), "clear-day": Image.open("sun.png"), "thunderstorm": Image.open("storm.png")}

year, month, day = str(date.today()).split('-')
week_index = date(int(year), int(month), int(day)).weekday()

def date_as_str():
    return f'{weekdays[week_index]},  {months[int(month)]} {int(day)}, {year}'

def time_as_str():
    time_str = time.strftime("%I:%M %p", time.localtime())
    if time_str[0:1] == "0":
        return time_str[1:]
    else:
        return time_str

def weekdays_str():
    sorted_weekdays = []
    i = week_index + 1
    for _ in range(7):
        sorted_weekdays.append(weekdays[i])
        i = 0 if i+1>6 else i + 1
    return "\n".join(i[0:3] for i in sorted_weekdays)

def weekly_lows_str():
    low_temps = weather_obj.getWeeklyMin()
    return "\n".join("%.1f" % i for i in low_temps[0:7])

def weekly_highs_str():
    high_temps = weather_obj.getWeeklyMax()
    return "\n".join("%.1f" % i for i in high_temps[0:7])

def getWeatherIcon():
    icon = weather_obj.getCurrentIcon()
    if icon in large_icons:
        img = large_icons[icon]
    else:
        img = large_icons['clear-day']
    p = PhotoImage(img)
    if icon in ("cloudy", 'partly-cloudy-day', 'rain', 'foggy'):
        p.__dict__['shift_amt'] = 15
    return p

def getWeekIcons():
    icons = weather_obj.getWeekIcons()
    icon_images = []
    for i in icons[0:7]:
        if i in small_icons:
            l = PhotoImage(small_icons[i])
            icon_images.append(l)
            if i in ("partly-cloudy-day", "cloudy", 'foggy'):
                l.__dict__['shift_amt'] = -5
                l.__dict__['vshift_amt'] = 5
            if i in ("rain"):
                l.__dict__['shift_amt'] = -5
                l.__dict__['vshift_amt'] = -2      
        else:
            icon_images.append(PhotoImage(small_icons['clear-day']))
    return icon_images

def current_temp_str():
    return "%.1f°" % weather_obj.getCurrentTemp()

def current_headline_str():
    return "\n".join(news_obj.topFiveHeadlines())

def dailyQuote():
    quote, author = quotes.getDailyQuote()
    quote_words = quote.split()
    quote_str = ""
    i = 0
    for words in quote_words:
        if i == 8:
            quote_str += "\n"
            i = 0
        quote_str += " " + words
        i += 1
        
    return quote_str + author




        
        

    
    


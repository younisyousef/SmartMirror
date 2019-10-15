from tkinter import Tk, Canvas, BOTH, BOTTOM, LEFT, Label, font
from PIL import Image
import model
FONT = "myriad"
HEADER_SIZE = 60


def date_label(root):
    return Label(root, text = model.date_as_str(), font = (FONT, HEADER_SIZE - 30), fg = "white", bg = "black")

def time_label(root):
    return Label(root, text = model.time_as_str(), font = (FONT, HEADER_SIZE), fg = "white", bg = "black")

def current_temp_label(root):
    return Label(root, text = model.current_temp_str(), font = (FONT, HEADER_SIZE), fg = "white", bg = "black")

def weekdays_label(root):
    return Label(root, text = model.weekdays_str(), font = (FONT, HEADER_SIZE - 30), fg = "white", bg = "black", justify = LEFT)

def weekly_lows_label(root):
    return Label(root, text = model.weekly_lows_str(), font = (FONT, HEADER_SIZE - 30), fg = "white", bg = "black")
    
def weekly_highs_label(root):
    return Label(root, text = model.weekly_highs_str(), font = (FONT, HEADER_SIZE - 30), fg = "white", bg = "black")

def current_weather_icon(root):
    img = model.getWeatherIcon()
    l = Label(root, image = img, borderwidth = 0, highlightthickness = 0)
    l.photo = img 
    if 'shift_amt' in img.__dict__:
            l.__dict__['shift_amt'] = img.shift_amt
    return l

def week_icon_labels(root):
    week_labels = []
    for i in model.getWeekIcons():
        l = Label(root, image = i, borderwidth = 0, highlightthickness = 0)
        l.photo = i
        if 'shift_amt' in i.__dict__:
            l.__dict__['shift_amt'] = i.shift_amt
        if 'vshift_amt' in i.__dict__:
            l.__dict__['vshift_amt'] = i.vshift_amt
        week_labels.append(l)
    return week_labels

def forcast_title(root):
    l = Label(root, text = "________________________________", font = (FONT, HEADER_SIZE-  40), fg = "white", bg = "black")
    f = font.Font(l, l.cget("font"))
    f.configure(underline = True)
    l.configure(font = f)
    return l

def top_headlines_label(root):
    return Label(root, text = model.current_headline_str(), font = (FONT, HEADER_SIZE - 45), fg = "white", bg = "black", justify = "left")

def quote_label(root):
    return Label(root, text = model.dailyQuote(), font = (FONT, HEADER_SIZE - 45), fg = "white", bg = "black", justify = "center")





        
        
    
        

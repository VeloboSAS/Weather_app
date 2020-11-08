from tkinter import *
from tkinter import messagebox
import requests


def get_weather(city):
    key = ''
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    if result:
        json = result.json()
        # (City, Country, temp_celsius, temp_fahrenheit, icon, weather)
        city = json['name']
        country = json['sys']['country']
        temp_celsius = json['main']['temp']
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temp_celsius, icon, weather)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        temp_lbl['text'] = '{:.2f}°C'.format(weather[2])
        weather_lbl['text'] = weather[4]
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


app = Tk()
app['bg'] = '#fafafa'
app.title('Weather app')
app.geometry('500x300')
app.wm_attributes('-alpha', 0.9)

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search weather', width=20, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font=('bold', 30))
location_lbl.pack()

temp_lbl = Label(app, text='')
temp_lbl.pack()

weather_lbl = Label(app, text='')
weather_lbl.pack()

app.mainloop()

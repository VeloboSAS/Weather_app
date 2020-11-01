from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests


#url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

#config_file = 'config.ini'
#config = ConfigParser()
#config.read(config_file)
#api_key = config['api_key']['key']

#key = 'edf5f5b43a633c3d6c4191acd3562b68'
#url = 'http://api.openweathermap.org/data/2.5/weather'
#params = {'APPID': api_key, 'q': city, 'units': 'metric'}

def get_weather(city):
    #result = requests.get(url.format(city, api_key))
    key = '6d00d1d4e704068d70191bad2673e0cc'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    if result:
        json = result.json()
        # (City, Country, temp_celsius, temp_fahrenheit, icon, weather)
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin  # - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 2
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temp_celsius, temp_fahrenheit, icon, weather)
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        #image['bitmap'] = 'weather_icons/{}@2x.png'.format(weather[4])
        #temp_lbl['text'] = '{:.2f}°C', '{:.2f}°F'.format(weather[2], weather[3])
        temp_lbl['text'] = '{:.2f}°C'.format(weather[2])
        weather_lbl['text'] = weather[5]
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


app = Tk()
app.title('Weather app')
app.geometry('500x300')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search weather', width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font=('bold', 20))
location_lbl.pack()

#image = Label(app, bitmap='')
#image.pack()

temp_lbl = Label(app, text='')
temp_lbl.pack()

weather_lbl = Label(app, text='')
weather_lbl.pack()

app.mainloop()

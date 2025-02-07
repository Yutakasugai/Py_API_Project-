import threading
import tkinter as tk
from tkinter.constants import E, LEFT, NE, NW, W
from time import *
from typing import Sized
import requests
import json
import webbrowser
from threading import *
import os
import sys

# Need to find the icon's location this way so we can create executable file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(
            os.path.abspath(__file__)))
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class liveStat:
    def __init__(self, master):
        self.master = master
        self.master.title("Live Stat")
        self.master.geometry("500x700")
        self.master.resizable(width=0, height=0)
        self.logo = tk.PhotoImage(file="basketball2.gif")
        self.w1 = tk.Label(self.master, image=self.logo).pack(
            side="top", anchor=NW)
        self.master.configure(bg='#fae6c3')
        self.time()
        self.btn = tk.Button(self.master, text="NBA games",
                             padx=10, pady=10, command=lambda: self.threading('NBAGame'))
        self.btn.place(relx=0.25, rely=0.10)

        self.btn2 = tk.Button(self.master, text="CBC News",
                              padx=10, pady=10, command=lambda: self.threading('CBCNews'))
        self.btn2.place(relx=0.55, rely=0.10)

        self.btn3 = tk.Button(self.master, text="Load",
                              padx=0.10, pady=10, command=lambda: self.threading('Load'))

        self.btn3.place(relx=0.75, rely=0.10)

    # Create a thread to run every function
    def threading(self, keyword):
        try:
            # call work funtion
            if (keyword == 'NBAGame'):
                t1 = Thread(target=self.NBAGame)
                t1.start()
            if (keyword == 'CBCNews'):
                t2 = Thread(target=self.CBCNews)
                t2.start()
            if (keyword == 'Load'):
                t3 = Thread(target=self.Load)
                t3.start()

        except Exception as e:
            print(str(e))

    def NBAGame(self):
        url_Game = 'https://www.nba.com/games'
        webbrowser.open(url_Game)

    def CBCNews(self):
        url_News = 'https://www.cbc.ca/news'
        webbrowser.open(url_News)

    def Load(self):
        for i in range(1000000):
            print(i)

    def time(self):
        string = strftime('%H:%M:%S %p')
        self.clock = tk.Label(self.master, text=string,
                              font='Verdana 13 bold', bg='#fae6c3')
        self.clock.place(relx=0.80, rely=0.01)
        self.clock.after(1000, self.time)

    def weather(self):
        # Create the label on the top
        self.label = tk.Label(self.master, text="Weather Update", font=(
            'Verdana 13 bold', 24), bg='#fae6c3')
        self.label.place(relx=0.48, rely=0.21, anchor='center')

        # Request the api to collect the data for London
        api_london = requests.get(
            "https://api.weatherapi.com/v1/forecast.json?key=332df27dce6d44f89a553830211012&q=London&days=1&aqi=yes&alerts=no")

        api = json.loads(api_london.content)

        country = api['location']['name']
        aveg_temp = api['forecast']['forecastday'][0]['day']['avgtemp_c']
        condition = api['forecast']['forecastday'][0]['day']['condition']['text']

        self.api = tk.Label(
            self.master, text=country + "    " + condition + "    " + str(
                aveg_temp) + "°", font=('Verdana 13 bold', 22), bg='#fae6c3')
        self.api.place(relx=0.50, rely=0.28, anchor='center')

        # Request the api to collect the data for Vancouver
        api_vancouver = requests.get(
            "https://api.weatherapi.com/v1/forecast.json?key=332df27dce6d44f89a553830211012&q=Vancouver&days=1&aqi=yes&alerts=no")
        api2 = json.loads(api_vancouver.content)

        print(api2['forecast']['forecastday'][0]['day']['condition']['text'])

        country2 = api2['location']['name']
        aveg_temp2 = api2['forecast']['forecastday'][0]['day']['avgtemp_c']
        condition2 = api2['forecast']['forecastday'][0]['day']['condition']['text']

        self.api_van = tk.Label(
            self.master, text=country2 + "    " + condition2 + "    " + str(
                aveg_temp2) + "°", font=('Verdana 13 bold', 22), bg='#fae6c3')
        self.api_van.place(relx=0.48, rely=0.36, anchor='center')

        # Request the api to collect the data for Tokyo
        api_tokyo = requests.get(
            "https://api.weatherapi.com/v1/forecast.json?key=332df27dce6d44f89a553830211012&q=Tokyo&days=1&aqi=yes&alerts=no")
        api3 = json.loads(api_tokyo.content)

        country3 = api3['location']['name']
        aveg_temp3 = api3['forecast']['forecastday'][0]['day']['avgtemp_c']
        condition3 = api2['forecast']['forecastday'][0]['day']['condition']['text']

        self.api_tokyo = tk.Label(
            self.master, text=country3 + "    " + condition3 + "    " + str(
                aveg_temp3) + "°", font=('Verdana 13 bold', 22), bg='#fae6c3')
        self.api_tokyo.place(relx=0.49, rely=0.44, anchor='center')

    def soccer_game(self):
        self.title = tk.Label(self.master, text="Today's Football Games", font=(
            'Verdana 13 bold', 23), bg='#fae6c3')
        self.title.place(relx=0.49, rely=0.56, anchor='center')

        api_request = requests.get(
            "https://api.weatherapi.com/v1/sports.json?key=332df27dce6d44f89a553830211012&q=London")
        api = json.loads(api_request.content)

        stadium = api['football'][0]['stadium']
        # country = api['football'][0]['country']
        game = api['football'][0]['match']

        self.foot_game = tk.Label(
            self.master, text="---" + stadium + "---" + "\n" + game, font=('Verdana 13 bold', 17), bg='#fae6c3')
        self.foot_game.place(relx=0.49, rely=0.65, anchor='center')

        stadium2 = api['football'][1]['stadium']
        game2 = api['football'][1]['match']

        self.foot_game2 = tk.Label(
            self.master, text="---" + stadium2 + "---" + "\n" + game2, font=('Verdana 13 bold', 17), bg='#fae6c3')
        self.foot_game2.place(relx=0.49, rely=0.75, anchor='center')

        stadium3 = api['football'][2]['stadium']
        game3 = api['football'][2]['match']

        self.foot_game3 = tk.Label(
            self.master, text="---" + stadium3 + "---" + "\n" + game3, font=('Verdana 13 bold', 17), bg='#fae6c3')
        self.foot_game3.place(relx=0.49, rely=0.85, anchor='center')


def main():
    win = tk.Tk()
    app = liveStat(win)
    app.weather()
    app.soccer_game()
    win.mainloop()


if __name__ == '__main__':
    main()

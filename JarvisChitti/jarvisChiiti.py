import subprocess
import sys

import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import PyQt5
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil

from click import clear
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# import PyQt5.uic.loadUiType
from JarvisGUIChitti import Ui_MainWindow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")
    speak("I am your Jarvis 1 point o , your Assistant  Sir, Please tell me how can I help you")

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        # Enable low security in gmail
        server.login('akashsingh285285@gmail.com', '285285@gmail.com')
        server.sendmail('akashsingh285285@gmail.com', to, content)
        server.close()

def usrname(self):
    speak("What should i call you sir")
    uname = self.takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")

class Mainthread(QThread):
    def __init__(self):
        super(Mainthread,self).__init__()
    def run(self):
        self.TaskExecution

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            speak("Say that Again sir!")
            return "None"
        query = self.query.lower()
        return self.query

    # def usrname(self):
    #     speak("What should i call you sir")
    #     uname = self.takeCommand()
    #     speak("Welcome Mister")
    #     speak(uname)
    #     columns = shutil.get_terminal_size().columns
    #
    #     print("#####################".center(columns))
    #     print("Welcome Mr.", uname.center(columns))
    #     print("#####################".center(columns))
    #
    #     speak("How can i Help you, Sir")

    def TaskExecution(self):
        wishMe()
        while True:

            self.query =self.takeCommand().lower()

            # All the commands said by user will be
            # stored here in 'query' and will be
            # converted to lower case for easily
            # recognition of command
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query :
                speak("Here you go to Youtube\n")
                webbrowser.open("youtube.com")

            elif 'open google' in self.query :
                speak("Here you go to Google\n")
                webbrowser.open("google.com")

            elif 'open stackoverflow' in self.query :
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")

            elif 'play music' in self.query  or "play song" in self.query :
                speak("Here you go with music")
                # music_dir = "G:\\Song"
                music_dir = "C:\\Users\\GAURAV\\Music"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))

            elif 'the time' in self.query :
                now = datetime.now()

                current_time = now.strftime("%H:%M:%S")
                print("Current Time =", current_time)
                speak(f"Sir, the time is {current_time}")

            elif 'open opera' in self.query :
                codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
                os.startfile(codePath)

            elif 'email to gaurav' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    to = "Receiver email address"
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'send a mail' in self.query :
                try:
                    speak("What should I say?")
                    content = self.takeCommand()

                    to = "prathvi285285@gmail.com "
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'how are you' in self.query :
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in self.query  or "good" in self.query :
                speak("It's good to know that your fine")

            elif "change my name to" in self.query :
                self.query  = self.query.replace("change my name to", "")
                assname = self.query

            elif "change name" in self.query :
                speak("What would you like to call me, Sir ")
                assname = self.takeCommand()
                speak("Thanks for naming me")

            elif "what's your name" in self.query  or "What is your name" in self.query :
                speak("My friends call me")
                speak(assname)
                print("My friends call me", assname)

            elif 'exit' in self.query :
                speak("Thanks for giving me your time")
                exit()

            elif "who made you" in self.query  or "who created you" in self.query :
                speak("I have been created by Gaurav.")

            elif 'joke' in self.query :
                speak(pyjokes.get_joke())

            elif "calculate" in self.query:

                app_id = "Wolframalpha api id"
                client = wolframalpha.Client(app_id)
                indx = self.query.lower().split().index('calculate')
                self.query  = self.query.split()[indx + 1:]
                res = client.self.query (' '.join(self.query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            elif 'search' in self.query  or 'play' in self.query :

                self.query  = self.query .replace("search", "")
                self.query  = self.query .replace("play", "")
                webbrowser.open(self.query )

            elif "who i am" in self.query :
                speak("If you talk then definately your human.")

            elif "why you came to world" in self.query :
                speak("Thanks to Gaurav. further It's a secret")

            elif 'power point presentation' in self.query :
                speak("opening Power Point presentation")
                power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
                os.startfile(power)

            elif 'is love' in self.query:
                speak("It is 7th sense that destroy all other senses")

            elif "who are you" in self.query:
                speak("I am your virtual assistant created by Gaurav")

            elif 'reason for you' in self.query:
                speak("I was created as a Minor project by Mister Gaurav ")

            elif 'change background' in self.query:
                ctypes.windll.user32.SystemParametersInfoW(20,
                                                           0,
                                                           "Location of wallpaper",
                                                           0)
                speak("Background changed succesfully")

            elif 'open bluestack' in self.query:
                appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
                os.startfile(appli)

            elif 'news' in self.query:

                try:
                    jsonObj = urlopen(
                        '''https://newsapi.org/v1/articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                    data = json.load(jsonObj)
                    i = 1

                    speak('here are some top news from the times of india')
                    print('''=============== TIMES OF INDIA ============''' + '\n')

                    for item in data['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                except Exception as e:

                    print(str(e))


            elif 'lock window' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'shutdown system' in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")

            elif "don't listen" in self.query or "stop listening" in self.query:
                speak("for how much time you want to stop jarvis from listening commands")
                a = int(self.takeCommand())
                time.sleep(a)
                print(a)

            elif "where is" in self.query:
                self.query = self.query.replace("where is", "")
                location = self.query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")

            elif "camera" in self.query or "take a photo" in self.query:
                ec.capture(0, "Jarvis Camera ", "img.jpg")

            elif "restart" in self.query:
                subprocess.call(["shutdown", "/r"])

            elif "hibernate" in self.query or "sleep" in self.query:
                speak("Hibernating")
                subprocess.call("shutdown / h")

            elif "log off" in self.query or "sign out" in self.query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif "write a note" in self.query:
                speak("What should i write, sir")
                note = self.takeCommand()
                file = open('jarvis.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = self.takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("jarvis.txt", "r")
                print(file.read())
                speak(file.read(6))

            elif "update assistant" in self.query:
                speak("After downloading file please replace this file with the downloaded one")
                url = '# url after uploading file'
                r = requests.get(url, stream=True)

                with open("Voice.py", "wb") as Pypdf:

                    total_length = int(r.headers.get('content-length'))

                    for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                           expected_size=(total_length / 1024) + 1):
                        if ch:
                            Pypdf.write(ch)

            # NPPR9-FWDCX-D2C8J-H872K-2YT43
            elif "jarvis" in self.query:

                wishMe()
                speak("Jarvis 1 point o in your service Mister")
                speak(assname)

            elif "weather" in self.query:

                # Google Open weather website
                # to get API of Open weather
                api_key = "Api key"
                base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
                speak(" City name ")
                print("City name : ")
                city_name = self.takeCommand()
                complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                response = requests.get(complete_url)
                x = response.json()

                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in kelvin unit) = " + str(
                        current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                        current_pressure) + "\n humidity (in percentage) = " + str(
                        current_humidiy) + "\n description = " + str(weather_description))

                else:
                    speak(" City Not Found ")

            elif "send message " in self.query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body=self.takeCommand(),
                    from_='Sender No',
                    to='Receiver No'
                )

                print(message.sid)

            elif "wikipedia" in self.query:
                webbrowser.open("wikipedia.com")

            elif "Good Morning" in self.query:
                speak("A warm" + self.query)
                speak("How are you Mister")
                speak(assname)

            # most asked question from google Assistant
            elif "will you be my gf" in self.query or "will you be my bf" in self.query:
                speak("I'm not sure about, may be you should give me some time")

            elif "how are you" in self.query:
                speak("I'm fine, glad you me that")

            elif "i love you" in self.query:
                speak("It's hard to understand")

            elif "what is" in self.query or "who is" in self.query:

                # Use the same API key
                # that we have generated earlier
                client = wolframalpha.Client("API_ID")
                res = client.self.query(self.query)

                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No results")
startExecution=Mainthread()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../Assistent_gif/main.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../Assistent_gif/T8bahf.gif")  # 20April
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startExecution.start()

    def showtime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())



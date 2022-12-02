import subprocess
import sys

import keyboard as keyboard
import kit as kit
import pywhatkit
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import PyQt5
import requests
import wikipedia

import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
from bs4 import BeautifulSoup
from requests import get
import shutil

from click import clear
from pywikihow import WikiHow
from requests import get
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pywhatkit
from PyQt5.QtWidgets import *
# import PyQt5.uic.loadUiType
from JarvisGUI import Ui_MainWindow
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[0].id)


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


def search_wikiHow(query, max_result=10, lang="en"):
    return list(WikiHow.search(query, max_result, lang))

def whatsupp(number,message):
    numb='+91'+number
    mess=message
    open_chat="https://web.whatsupp.com/send?photo="+ numb +'&text='+mess
    webbrowser.open(open_chat)
    time.sleep(15)
    keyboard.press('enter')

def whatsupp_Grp(group_id,message):
    open_chat = "https://web.whatsupp.com/accept?code=" + group_id
    webbrowser.open(open_chat)
    time.sleep(15)
    keyboard.write(message)
    time.sleep(1)
    keyboard.press('enter')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('akashsingh285285@gmail.com', 'sky285285')
    server.sendmail('akashsingh285285@gmail.com', to, content)
    server.close()


def speak_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=yourapikey'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Source: The Times Of India')
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts) - 1:
            break
        speak('Moving on the next news headline..')
    speak('These were the top headlines, Have a nice day Sir!!..')


class Mainthread(QThread):
    def __init__(self):
        super(Mainthread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            # r.adjust_for_ambient_noise(source)
            audio = r.listen(source,timeout=5)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            speak("Say that Again sir! please")
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
            self.query = self.takeCommand()
            # All the commands said by user will be
            # stored here in 'query' and will be
            # converted to lower case for easily
            # recognition of command
            if 'Wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
                print(results)


            # elif "you can sleep now " in self.query:
            #     speak("Okey Sir im going to sleep know sir , you can call me anytime ..")
            #     break

            elif"  my IP address" in self.query:
                ip=get("https://api.ipify.org").text
                speak(f"Your Ip Address is {ip}")

            elif "open Notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif 'open sublime text' in self.query:
                apath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
                os.startfile(apath)

            elif 'open command prompt' in self.query:
                os.system('start cmd')

            elif "Search on chrome" in self.query:
                speak("what should i search ,Sir")
                search = self.takeCommand()
                chrompath = "C:\\Users\\akash singh\\AppDataLocal\\Google\\Chrome\\Application\\chrome.exe %s"
                webbrowser.get(chrompath).open_new_tab(search + ".com")
            # elif "temperature" in self.query:
            #     search="temperature in Agra"
            #     url =f"https://www.google.com/search?q(search)"
            #     r=requests.get(url)
            #     data=BeautifulSoup(r.text,"html.parser")
            #     temp=data.find(("div",classs="BNeawe").text
            #     speak(f"current(search) is (temp)")

            elif 'open stackoverflow' in self.query:
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("stackoverflow.com")
# working
            elif 'play music' in self.query or "play song" in self.query:
                speak("Here you go with music")
                # music_dir = "G:\\Song"
                music_dir = "F:\mymovei"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))
 # working
            elif 'what is the time now' in self.query:
                strTime=datetime.datetime.now().strftime("%H:%M,%S")
                print(strTime)
                speak(f"Sir ,the Time is {strTime}")

            elif 'send SMS' in self.query:
                speak("sir what should I say")
                msk=self.takeCommand()

                from twilio.rest import Client

                account_sid='ACc6bf0b7ad9ef655e9123225cf20d000c'
                auto_token='719d8c1c6b79bc267b6fcb0d7df2e956'

                client=Client(account_sid,auto_token)

                message=client.messages \
                    .create(
                       body=msk,
                       from_='+13608136365',
                       to="+916396881542"
                     )
                print(message.sid)


            elif 'open opera' in self.query:
                codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
                os.startfile(codePath)

 # working
            elif 'send a mail to Raju' in self.query:
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    to = "rajneeshkumar27042000@gmail.com "
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
 # working
            elif 'how are you' in self.query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in self.query or "good" in self.query:
                speak("It's good to know that your fine")

            elif "change my name to" in self.query:
                self.query = self.query.replace("change my name to", "")
                assname = self.query

            elif "my ip address" in self.query:
                ip=get('https://api.ipify.org').text
                speak(f"Your IP address is{ip}")

            elif "change name" in self.query:
                speak("What would you like to call me, Sir ")
                assname = self.takeCommand()
                speak("Thanks for naming me")

            elif "what's your name" in self.query or "What is your name" in self.query:
                speak("My friends call me  ,Jarvis bro")

                print("My friends call me Jarvis bro")

            elif 'exit' in self.query:
                speak("Thanks for giving me your time")
                exit()

            elif "who made you" in self.query or "who created you" in self.query:
                speak("I have been created by Akash Singh. Thank you Akash Sir")

            elif 'joke' in self.query:
                speak(pyjokes.get_joke())



            elif 'search' in self.query or 'play' in self.query:

                self.query = self.query.replace("search", "")
                self.query = self.query.replace("play", "")
                webbrowser.open(self.query)

            elif "who i am" in self.query:
                speak("If you talk then definately your human.")

            elif "why you came to world" in self.query:
                speak("Thanks to Akash... further It's a secret")

            elif 'power point presentation' in self.query:
                speak("opening Power Point presentation")
                power = r"C:\\Users\\Akash\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
                os.startfile(power)

            elif 'What is love' in self.query:
                speak("It is 7th sense that destroy all other senses")

            elif "who are you" in self.query:
                speak("I am your virtual assistant created by  Akash Singh")

            elif 'reason for you' in self.query:
                speak("I was created as a Minor project by Mister Akash Singh ")

            elif 'change background' in self.query:
                ctypes.windll.user32.SystemParametersInfoW(20,
                                                           0,
                                                           "Location of wallpaper",
                                                           0)
                speak("Background changed succesfully")


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

            # # elif 'lock window' in self.query:
            # #     speak("locking the device")
            # #     ctypes.windll.user32.LockWorkStation()


            # elif 'shutdown system' in self.query:
            #     speak("Hold On a Sec ! Your system is on its way to shut down")
            #     subprocess.call('shutdown / p /f')
            #
            # elif 'empty recycle bin' in self.query:
            #     winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            #     speak("Recycle Bin Recycled")

            # elif "don't listen" in self.query or "stop listening" in self.query:
            #     speak("for how much time you want to stop jarvis from listening commands")
            #     a = int(self.takeCommand())
            #     time.sleep(a)
            #     print(a)

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

            # elif "log off" in self.query or "sign out" in self.query:
            #     speak("Make sure all the application are closed before sign-out")
            #     time.sleep(5)
            #     subprocess.call(["shutdown", "/l"])

            elif "write a note" in self.query:
                speak("What should i write, sir")
                note = self.takeCommand()
                file = open('jarvis.txt', 'w')


            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("jarvis.txt", "r")
                print(file.read())
                speak(file.read(6))
            # how to do mode
            elif "activate how to do mod" in self.query:
                from pywikihow import search_wikihow
                speak("How to do mode is ,Activated now  ")
                while True:
                    speak("Please tell me sir , What you you want to know ")
                    how = self.takeCommand()
                    try:
                        if "exit" in how or "close " in how:
                            speak("Okey sir , how to do  mode is closed now")
                            break
                        else:
                            max_result = 1
                            how_to = search_wikiHow(how, max_result)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("sorry sir , I am not able to find this")
            #
            # elif "update assistant" in self.query:
            #     speak("After downloading file please replace this file with the downloaded one")
            #     url = '# url after uploading file'
            #     r = requests.get(url, stream=True)
            #
            #     with open("Voice.py", "wb") as Pypdf:
            #
            #         total_length = int(r.headers.get('content-length'))
            #
            #         for ch in progress.bar(r.iter_content(chunk_size=2391975),
            #                                expected_size=(total_length / 1024) + 1):
            #             if ch:
            #                 Pypdf.write(ch)

            # NPPR9-FWDCX-D2C8J-H872K-2YT43
            elif "Jarvis tell me your version" in self.query:

                wishMe()
                speak("Jarvis 1 point o in your service Mister")
                speak(assname)

            elif "where is" in self.query:
                self.query = self.query.replace("where is", "")
                location = self.query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")


            elif'send WhatsApp message' in self.query:
                speak("what should i say to Rajneesh ,Sir?")
                say=self.takeCommand()
                speak('set the time to deliever the message!! ')
                pywhatkit.sendwhatmsg('+919045633959',f'{say}',int(input()),int(input()))
                speak("message sent")



            elif"open youtube" in self.query:
                webbrowser.open("youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("facebook.com")

            elif"open stackoverflow" in self.query:
                webbrowser.open("stackoverflow.com")

            elif "Good Morning" in self.query:
                speak("A warm" + self.query)
                speak("How are you Mister")
                speak(assname)

            # most asked question from google Assistant
            elif "will you be my friend" in self.query or "will you be my friend" in self.query:
                speak("I'm not sure about, may be you should give me some time")

            elif "how are you" in self.query:
                speak("I'm fine, glad you me that and what about you Sir")

            elif "no thanks" in self.query:
                speak("thank for using me sir , have a good day .")
                sys.exit()
            speak("Sir do you have any other work for me ")



startExecution = Mainthread()


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


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())



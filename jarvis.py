from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import wolframalpha
from selenium import webdriver
import pyjokes
import json
import ctypes
import subprocess
import winshell
from urllib.request import urlopen
import time
import requests
import smtplib
import random
import socket
from colored import fg, attr
import re
from googletrans import Translator
from time import ctime
import urllib.request
import urllib.parse 
import pyautogui
import wmi
import psutil
import pyscreenshot
from twilio.rest import Client
import http.client
from gmusicapi import Mobileclient
import tkinter
import ta
from playsound import playsound as play

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('volume', 10.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    speak("Hello sir")

    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f"Its {strTime}")
    api_key = "2eb46814379c57417bd1558b695a3c4a"
    weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    location = str("Hyderabad")
    url = weather_url + "appid=" + api_key + "&q=" + location 
    js = requests.get(url).json() 
    if js["cod"] != "404": 
        desc = js["weather"][0]["description"]
        resp_string = " and weather is "+ str(desc) 
        speak(resp_string)

    speak("What do u want")       

def takecommand():
    #it takes microphone input from the user returns string output

    r = sr.Recognizer()
    while (1):

        try: 
            with sr.Microphone() as source:
                audio = r.listen(source)
                query=r.recognize_google(audio, language='en-in')
                print("Listening")
                if "hey jarvis" in query or "jarvis" in query or "hey" in query or "son" in query:
                    play('C:\\Users\\RUTHWIK\\Documents\\assistant\\dum.mp3')
                    audio = r.listen(source)
                    query=r.recognize_google(audio, language='en-in')
                    if 'open base' in query:
                        speak('opening base')
                        webbrowser.open("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

                    elif 'open chrome' in query:
                        speak('opening chrome')
                        webbrowser.open("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

                    elif 'open instagram' in query or 'Open Instagram' in query or 'open Instagram' in query or 'Open instagram' in query:
                        speak('opening instagram')
                        codepath = ("https://www.instagram.com/")
                        os.startfile(codepath)

                    elif 'search for' in query or "what is" in query or "who is" in query or "how is" in query:
                        query = query.replace("search for", "")
                        query = query.replace("what is", "")
                        query = query.replace("who is", "")
                        query = query.replace("how is", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak(results)

                    elif 'open gmail' in query or 'Check mail' in query:
                        speak('opening gmail')
                        codepath = ("https://mail.google.com/mail/u/0/?ogbl#inbox")
                        os.startfile(codepath)

                    elif 'task list' in query or 'tasklist' in query:
                        print('\n\tShowing All Running Tasks!')
                        speak('Showing All Running Tasks!')
                        subprocess.call('tasklist')
                        time.sleep(10)

                    elif 'open maps' in query:
                        codepath = ("https://www.google.com/maps")
                        os.startfile(codepath)

                    elif 'open drive' in query:
                        codepath = ("https://drive.google.com/drive/my-drive")
                        os.startfile(codepath)
                        time.sleep(3)

                    elif 'coronavirus cases in india' in query:
                        codepath = ("https://www.worldometers.info/coronavirus/country/india/")
                        os.startfile(codepath) 

                    elif "who are you" in query or "define yourself" in query: 
                        me = '''Hello, I am Jarvis Your personal Assistant.You can command me to perform various operations'''
                        speak(me)

                    elif 'open notepad' in query or 'open text document' in query:
                        speak('opening notepad')
                        codepath = ('C:\\Windows\\system32\\notepad.exe')
                        os.startfile(codepath)

                    elif "who made you" in query or "who created you" in query: 
                        made = "I was created by Ruthwik."
                        speak(made)

                    elif 'how are you' in query: 
                        speak("I am fine, Thank you") 
                        speak("How are you, Sir") 
            
                    elif 'i am fine' in query or "i am good" in query or "i'm fine" in query or "I'M fine" in query: 
                        amfine = [
                            'Its good to know that your fine sir',
                            'am glad that you are fine',
                            'have a great day sir',
                        ]
                        amfine = random.choice(amfine)
                        speak(amfine)

                    elif 'sucide' in query or 'close' in query: 
                        speak("as you wish sir") 
                        exit()

                    elif 'exit' in query or 'quit' in query:
                        quitApp()

                    elif 'tell me a joke' in query or "tell me another" in query: 
                        speak(pyjokes.get_joke())

                    elif 'lock window' in query: 
                            speak("locking the device") 
                            ctypes.windll.user32.LockWorkStation() 
            
                    elif 'shutdown system' in query or 'shutdown the pc' in query or 'shutdown' in query: 
                            speak("Hold On a Sec ! Your system is on its way to shut down") 
                            subprocess.call('shutdown/p') 
                            
                    elif 'empty trash' in query: 
                        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
                        speak("trash removed")

                    elif 'change background' in query: 
                        ctypes.windll.user32.SystemParametersInfoW(20,0,"location",0) 
                        speak("Background changed succesfully")

                    elif "where is" in query:
                        query = query.replace("where is", "") 
                        location = query 
                        speak("User asked to Locate") 
                        speak(location) 
                        os.startfile("https://www.google.com/maps/place/" + location + "")

                    elif "write a note" in query: 
                        speak("What should i write, sir") 
                        note = takecommand().lower() 
                        file = open('jarvis.txt', 'w') 
                        speak("Sir, Should i include date and time") 
                        snfm = takecommand().lower() 
                        if 'yes' in snfm or 'sure' in snfm: 
                            strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                            file.write(strTime) 
                            file.write(" :- ") 
                            file.write(note) 
                        else: 
                            file.write(note)

                    elif "don't listen" in query or "stop listening" in query: 
                        speak("for how much time you want to stop jarvis from listening commands") 
                        a = int(takecommand().lower()) 
                        time.sleep(a)

                    elif "take screenshot" in query or "take shot" in query:
                        speak("taking screenshot")
                        pic = pyautogui.screenshot()
                        pic.save("C:\\Users\\RUTHWIK\\Pictures\\pics")

                    elif "restart" in query: 
                        subprocess.call(["shutdown", "/r"]) 
                        
                    elif "hibernate" in query: 
                        speak("Hibernating") 
                        subprocess.call("shutdown / h") 

                    elif "amazon" in query:
                            webbrowser.open("https://www.amazon.in/s?k="+query.replace("on amazon","").replace("search ",""))    
                            speak("ok Sir!")
            
                    elif "log off" in query or "sign out" in query: 
                        speak("Make sure all the application are closed before sign-out") 
                        time.sleep(5) 
                        subprocess.call(["shutdown", "/l"])

                    if "close chrome" in query:
                        os.system("taskkill /im chrome.exe /f")

                    elif "good morning" in query or "good afternoon" in query: 
                        goodmorning = [
                            'A warm' +query,
                            'good morning',
                            'morning',
                        ]
                        goodmorning = random.choice(goodmorning)
                        speak(goodmorning)
                        speak("How are you sir")    

                    elif "send email" in query:
                        try:
                            speak("what should i say")
                            content = takecommand().lower()
                            to = "ruthwikcd@gmail.com"
                            sendEmail(to, content)
                            speak("email has been sent")
                        except Exception as e:
                            print(e)
                            speak("sorry am not able to send this email")

                    elif "wait" in query or 'google' in query or 'open chrome and search for' in query:
                        query = query.replace("wait", "")
                        query = query.replace(" for ", "")
                        query = query.replace(' google', '')
                        query = query.replace('google ', '')
                        query = query.replace('open chrome and search for', '')
                        webbrowser.open(f'https://www.google.com/search?q={query}')
                        print(f'\n\tSearching For "{query.title()}"')
                        speak(f"Searching for {query}")

                    elif 'send a box' in query: 
                        try: 
                            speak("What should I say?") 
                            content = takecommand().lower() 
                            speak("whom should i send") 
                            to = input()     
                            sendEmail(to, content) 
                            speak("Email has been sent !") 
                        except Exception as e: 
                            print(e) 
                            speak("I am not able to send this email")

                    elif '.' in query:
                        query = query.replace('open ', '')
                        print('\n\tOpening ' + query)
                        speak(f"Opening {query}!")
                        webbrowser.open('http://'+ query)

                    elif 'play' in query:
                        query = query.replace('play ', '')
                        musicSearch = f'https://music.youtube.com/search?q={query}'
                        print(f"\n\tPlaying {query} ")
                        speak(f'Playing {query}')
                        webbrowser.open(musicSearch)

                    elif 'launch' in query:
                        query = query.replace('launch ', "")
                        app = query.title()
                        try:
                            os.startfile(app)
                            print('\n\tLaunching ' + app.title())
                            speak(f'Launching {app}!')
                        except:
                            print(f"\n\tCouldn't Launch {app.title()}!Should I Search Online ?")
                            speak(f"Couldn't Launch {app}, Should I Search Online?")
                            reply = takecommand().lower()
                            if "yes" in reply or 'ok' in reply or 'yup' in reply or 'do' in reply:
                                print(f'\n\tSearching Online for {app}')
                                speak('Fine, Searching Online!')
                            else:
                                print("\n\tOkay! am sorry")
                                speak("Okay, am sorry")

                    elif 'my ip'in query or 'whats my ip' in query:
                        print('\n\tShowing!')
                        speak("Showing Ip Details")
                        subprocess.call("ipconfig")
                        time.sleep(2)

                    elif 'systeminfo' in query or 'system info' in query:
                        print('\n\tShowing System Information!\n')
                        speak("Ok, Showng Your System Information Please Wait")
                        subprocess.call('systeminfo')
                        speak('Done!')
                        time.sleep(5)

                    elif 'thanks jarvis' in query or 'thank you jarvis' in query:
                        thanksGiving = [
                            'Nevermind!',
                            'You are Always Welcome!',
                            'Mention Not!',
                            "That's My Duty!"
                        ]
                        thanksGiving = random.choice(thanksGiving)
                        print(f'\n\t{thanksGiving}')
                        speak(thanksGiving)

                    elif '©empty_^_^_queryª' in query:
                        print("  Did Not Get It...\n\n{}~\n")
                        speak('Did Not Get it!')

                    elif 'sorry' in query:
                        sorry = [
                            'its ok',
                            'its fine',
                            'not bad',
                        ]
                        sorry = random.choice(sorry)
                        speak(sorry)

                    elif 'open my facebook profile' in query:
                        codepath = ("https://www.facebook.com/ruthwikreddyyelchalla.351")
                        os.startfile(codepath)

                    elif "facebook" in query: 
                        query = query.replace("facebook", "") 
                        location = query 
                        speak(location) 
                        webbrowser.open("https://www.facebook.com/" + location + "")

                    elif 'gas' in query or 'Gas' in query:
                        speak(f'Ok!')
                        reg_ex = re.search('gas (.+)', query)
                        if reg_ex:
                            domain = query.split("gas",1)[1] 
                            query_string = urllib.parse.urlencode({"search_query" : domain})
                            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string) 
                            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode()) # finds all links in search result
                            webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
                            pass

        except sr.RequestError as e:
            print("Could not understand; {0}",format(e))

        except sr.UnknownValueError:
            pass

        except sr.WaitTimeoutError:
            pass

    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ruthwik131@gmail.com', 'yprasannar')
    server.sendmail('ruthwik131@gmail.com', to, content)
    server.close()

def quitApp():
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<18:
        print('\n\tBye {}, Have a Good Day!')
        speak('Bye {}, Have a Good Day!')
    else:
        print('\n\tBye {}, Good Night!')
        speak('Bye {}, Good Night!')
    print("\n\t<!!! OFFLINE !!!>")
    exit(0)

def media():
    speak('ok sir')
    speak('what do u want me to play sir')
    k = takecommand().lower()
    speak('ok sir playing' + k + 'for you')
    os.startfile('Z:\\Music' + k + '.mp3')

def connectionCheck():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('www.google.com', 80))
        s.close()
    except Exception:
        print('\n\tUnable to Connect!')
        speak('Unable to Connect!')
        quitApp()












       
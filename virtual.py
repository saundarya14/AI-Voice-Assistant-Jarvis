import ctypes
import datetime
import shutil
import subprocess
import time
import webbrowser
import os
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
import winshell as winshell
import wolframalpha
import json
from ecapture import ecapture as ec
from pyjokes import pyjokes

print('Loading your AI personal assistant, Hello, I am Jarvis')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def username():
    speak("What should i call you?")
    uname = takeCommand()
    speak("Welcome miss")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Ms.", uname.center(columns))
    print("#####################".center(columns))

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statements = r.recognize_google(audio, language='en-in')
            print(f"user said:{statements}\n")

        except Exception:
            speak("Pardon me, please say that again")
            return "None"
        return statements


speak("Loading your AI personal assistant, Hello, I am Jarvis")
username()
wishme()

if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Jarvis is shutting down,Good bye')
            print('your personal assistant Jarvis is shutting down,Good bye')
            break

        if 'who is ' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in statement or "how you doing" in statement:
            speak("I am fine, Thank you")
            speak("How are you?")

        elif 'fine' in statement or "good" in statement:
            speak("It's good to know that your fine")


        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "9e1fbe4eaf712580b5317e10eeaeeaf2"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x.get("main")
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidity) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Jarvis version 1 point O your personal assistant. I am programmed to do minor tasks like'
                  'opening youtube, google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Saundarya")
            print("I was built by Saundarya")

        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, 'test', "img.jpg")

        elif "play" in statement:
            songs = statement.replace('play', '')
            speak('playing ' + songs)
            pywhatkit.playonyt(songs)

        elif 'search ' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'joke' in statement:
            speak(pyjokes.get_joke())

        elif 'change background' in statement:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully")

        elif 'empty recycle bin' in statement:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")


        elif "write a note" in statement:
            speak("What should i write?")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Should i include date and time?")
            snf = takeCommand()
            if 'yes' in snf or 'sure' in snf:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in statement:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "YTR6KJ-WXWPP54V3L"
            client = wolframalpha.Client('YTR6KJ-WXWPP54V3L')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "restart" in statement:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in statement or "sleep" in statement:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)

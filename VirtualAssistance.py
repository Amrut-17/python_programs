import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 130)

# Speak the Given code of lines
def speak(text):
    engine.say(text)
    engine.runAndWait()

# WISH YOU w.r.t CURRENT TIME
def wishme():
    hour = datetime.datetime.now().hour
    # minutes = datetime.datetime.now().minute
    
    # speak('current time is '+ str(hour) + 'hours and'+ str(minutes)+ 'minutes')

    if hour >= 0 and hour < 12:
        speak('Good Morning Sir')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon Sir')

    else :
         speak('Good Evening Sir')

# TAKE INPUT OR COMMAND FROM USER THROUGH MICROPHONE
def inputcommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listining.....')
        audio = r.listen(source)

    try :
        print('Recognizing....')
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")
    except Exception as e:
        print('Say that again plese', e)
        query = None
    return query




wishme()

speak("    ")
# speak('I am your Virtual Assistance    ')
# speak('you can call me Tony    ')
speak('How may i help You      ')

query = inputcommand()

# LOGIC FOR BASIC TASKS W.R.T QUERY

if 'wikipedia' in query.lower():
    speak('Searching Wikipedia.....')
    speak('................')
    query = query.replace('wikipedia', "")
    results = wikipedia.summary(query, sentences = 2)
    print(results)
    speak(results)
elif 'open youtube' in query.lower() :
    # webbrowser.open('YouTube.com')
    url = "youtube.com"
    # anothtr = input()
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open google' in query.lower() :
    # webbrowser.open('YouTube.com')
    url = "https://www.google.com"
    # anothtr = input()
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open instagra' in query.lower():
    url = "https://www.instagram.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'open facebook' in query.lower():
    url = "https://www.facebook.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
elif 'search privately' in query.lower():
    url = "https://www.duckduckgo.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
else:
    speak('Not Recognize')


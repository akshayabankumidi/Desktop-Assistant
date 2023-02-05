import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyjokes
import os
from googlesearch import search

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)  
            command = command.lower()
            if 'sakura' in command:
                command = command.replace('sakura', '')
                print(command)
                return command
        return command
        
    except:
        pass
    return ' '


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who' in command:
        person = command.replace('who ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'local' in command:
        os.startfile(r'C:')
    elif 'screenshots' in command:
        os.startfile(r'C:\Users\Dolly\Pictures\Screenshots')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'student' in command:
        webbrowser.open("https://cmritautonomous.org/BeesERP/Login.aspx?ReturnUrl=%2fbeeserp%2fStudentLogin%2fMainStud.aspx")
    elif ' ' in command:
        talk("say that again please...")
    else:
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        s="https://www.google.com/search?q="
        temp=command
        news=""
        for i in temp:
            if(i==' '):
                news+='+'
            else:
                news+=i
        webbrowser.get('chrome').open_new_tab(s + news)


while True:
    run_alexa()
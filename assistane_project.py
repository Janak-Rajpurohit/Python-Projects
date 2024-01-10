
from codecs import StreamReaderWriter
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import  playsound
import os
from googlesearch import search

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[1])
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=21 and hour<24:
        speak("good night sir")
    elif hour>=5 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour>=18 and  hour<21:
        speak("good evening")

def  command():
    ## take command from user
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try :
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        #print(f"User said --> {query}")
    
    except Exception as e:
        # print(e)
        print("Say that again please.")
        return "None"
    return query

def sendemail(to,content):
    pass
    

### main

if __name__=="__main__":
    wishMe()
    while True:
        query=command().lower()
        if  query == "bye":
            speak("goodbye")
            exit()
        elif "wikipedia"  in query :
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif  "open youtube" in query:
            webbrowser.open('www.youtube.com')
        elif "open goggle" in query:
            webbrowser.open('www.google.com')
        elif "open" in query:
            q=query.split(" ")[1]
            webbrowser.open(f"www.{q}.com")
        elif "play music" in query:
            print("playing...")
            # playsound("C:\\PYTHON_PROGRAMS")
            music_dir="C:\\music"
            songs=os.listdir(music_dir)
            print(enumerate(songs))
            n=int(input("Enter song number > "))
            os.startfile(os.path.join(music_dir,songs[n]))

        elif "the time" in query:
            dt=datetime.datetime.now().strftime("%H:%M:%S")
            # t=dt.time()
            print(dt)
            speak(f"Sir the time  is {dt}")
            # speak(f"{dt.hour} hours ,{dt.minute} minute")

        elif "the date" in query:
            dt=datetime.datetime.now().strftime("%w %B")
            speak(f"Sir the date is {dt}")

        elif "visual studio code" in query:
            codePath="C:\\vs code\\Code.exe"
            os.startfile(codePath)

        elif "send email" in query:
            try:
                speak("What should i say.")
                content=command()
                to="janakrajpurohit612@gmail.com"o
                sendemail(to,content)
                speak("email has been send.")
            except Exception as e:
                print(e)
                speak("Sorry ,not able to send email.")

        elif "search" in query:
            q=query.split(" ")[1]
            searched=search(q,tld="co.in",num=10,stop=10,pause=2)
            for j in  searched:
                webbrowser.open(j)
                break


    







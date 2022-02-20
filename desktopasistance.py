import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import pywhatkit
import flask

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")  
    speak("this is hash, a desktop assistance made by Anuj, Sir how may i help you") 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.5
        audio = r.listen(source) 
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en,hi-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)

        print("say that again please..")
        return "None"
    return query
def sendEmail(to, content):
    server =smtplib.Smtp('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bondrock757@gmail.com','anuj.@9698')
    server.sendmail('bondrock757@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=4)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir ='E:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            d = random.choice(songs)
            print(d)
            songs= os.listdir(music_dir)
            print(songs)
            song = random.choice(songs)
            chosensong =(music_dir)
            os.startfile(os.path.join(music_dir,song))

        elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir, the time is{strTime}")
        elif 'open code' in query:
            codepath ="C:\\Users\\rajan\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "rajanuj826@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry my friend i m not able to sent this email")
                
        elif 'play song on youtube' in query:
            
            speak('which should i play')
            audio = takeCommand()
            pywhatkit.playonyt(audio)
            speak('here is the song')
            print ('here is the song')


        elif 'exit' in query:
            speak('hash is signing off, Good bye')
            quit()
         
         
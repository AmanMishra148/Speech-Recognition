import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
#print(voices)
engine.setProperty("voice", voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("good morning!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("I am Jarvis Sir . Please tell me how may i help you")
    #if __name__ == "__main__":
    #    wishMe()
     #   takeCommand()
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email',"your password")
    server.sendmail("your email", to, content)
    server.close()


"""
it takes microphone input from the user and returns string output
"""
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening............")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("recognising.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)

        print("say that again please...")
        return "None"
    return query





if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "what is the weather" in query:
            webbrowser.open("accuweather.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif "open code" in query:
            codepath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "send email" in query:
            try:
                speak("tell the message?")
                content = takeCommand()
                to = "reciever's mail"
                sendEmail =(to, content)
                speak("Email has been sent")

            except exception as e:
                print("e")

        elif "stop" in query:
            exit(1)
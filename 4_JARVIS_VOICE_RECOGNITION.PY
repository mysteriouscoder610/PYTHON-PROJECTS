import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pyjokes
import os
def sptext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("Recognising...")
            data = r.recognize_google(audio)
            print(data)
            return data  # Returning the recognized text
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return ""  # Return an empty string in case of error

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        data1 = sptext().lower()  # Move this inside the loop to keep updating data1

        if "name" in data1:
            name = "My name is Ayush"
            speechtx(name)
        elif "old are you" in data1:
            age = "I am two years old"
            speechtx(age)
        elif 'time' in data1:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speechtx(time)
        elif 'code' in data1:
            webbrowser.open("https://codeforces.com/")
            speechtx("Opening Codeforces")
        elif "joke" in data1:
            joke_1 = pyjokes.get_joke(language="en", category="neutral")
            print(joke_1)
            speechtx(joke_1)
        elif 'play song' in data1:
            add = "D:\music"
            listsong = os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add, listsong[0]))
        # elif 'whatsapp' in data1:
        #     add = 
        elif "exit" in data1:
            speechtx("Thank you")
            break
        
        # above line will give the 5 sec delay

input("Press Enter to exit...")

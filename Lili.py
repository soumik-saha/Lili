import speech_recognition as sr
import pyttsx3
import pywhatkit as pwk
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    # engine.say('Hello Soumik, I am your Alexa! What can I do for you?')
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('Alexa is listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                # command = command.replace('alexa ','')
                print(command)
    except:
        pass
    if 'alexa' in command:
        command = command.replace('alexa ','')
        return command
def run_alexa():
    command = take_command()
    if 'play' in command:
        command = command.replace('play','Playing')
        song = command.replace('Playing','')
        talk(command)
        print(command)
        pwk.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
        print(time)
    elif 'date' in command:
        date = datetime.datetime.today().strftime('%d-%m-%y')
        talk('Current date is' + date)
        print(date)
    elif 'wikipedia' in command:
        search = command.replace('wikipedia','')
        info = wikipedia.summary(search, 1)      
        print(info)
        talk(info)
    elif 'are you single' in command:
        ans = 'No, I\'m in a relationship with Soumik'
        print(ans)
        talk(ans)
    elif 'joke' or 'jokes' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        talk('Please say command again!')

while True:
    run_alexa()
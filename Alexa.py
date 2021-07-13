import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass

    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        talk('yeah sure')
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        talk('what is your next command?')
    elif 'joke' in command:
        talk('yeah sure')
        talk(pyjokes.get_joke())
        talk('what is your next command?')
    elif 'time' in command:
        talk('yeah sure')
        time = datetime.datetime.now().strftime('%I:%M %p')
        # %I means 12 hour format of time, %p for am or pm
        print(time)
        talk('Current time is ' + time)
        talk('what is your next command?')
    else:
        talk('Please repeat your command')


while True:
    run_alexa()

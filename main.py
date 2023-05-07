import speech_recognition as sr
import pyttsx3

eng = pyttsx3.init()
female_voice = eng.getProperty('voices')[1].id  # get the female voice
eng.setProperty("voice", female_voice)  # set the female voice

flag = True

# recognize the audio
def recognize():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        audio = recognizer.listen(source)

        try:
            return recognizer.recognize_google(audio)
        except:
            say("Can you say again")
            recognize()

# predict the answer
def predict_answer(question):
    if all(i in question.lower() for i in ["your", "name"]):
        return "I'm your google assistant"

    say("Can you ask another question")
    recognize()

# say the text
def say(answer):
    eng.say(answer)
    eng.runAndWait()

while flag:
    say("Please ask your question")
    say(predict_answer(recognize()))

    while True:
        say("Do you have any question")
        answer = recognize()

        if answer == 'yes':
            break
        elif answer == 'no':
            flag = False
            say("Have a nice day")
            break

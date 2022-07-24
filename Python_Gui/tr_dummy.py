import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound
import os

r = sr.Recognizer()
translator=google_translator()

mc = sr.Microphone()


with mc as source:
    audio = r.listen(source)
    try:
        speech_text = r.recognize_google(audio)
        print(speech_text)
    except sr.UnknownValueError:
        print("could not listen")
    except sr.RequestError:
        print("could not request")

    translated_text=translator.translate(speech_text,lang_tgt='fr')
    print(translated_text)

    voice=gTTS(translated_text,lang='fr')
    voice.save("goal.mp3")
    playsound('goal.mp3')
    # os.remove('goal.mp3')
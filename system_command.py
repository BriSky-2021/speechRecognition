import os
import speech_recognition as sr
from os import path

class event_operation:

    def open_notepad(self):
        os.system('start notepad')

    def play_music(self):
        os.system('start english.wav')

    def push_button(self):
        # 读音乐
        r = sr.Recognizer()
        audio=None

        if True:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)

        if False:
            AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")

            with sr.AudioFile(AUDIO_FILE) as source:
                audio = r.record(source)  # read the entire audio file



        recognize_text=None

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            recognize_text=r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return 1
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return 1


        if(recognize_text!=None):
            if recognize_text=='one two three':
                self.open_notepad()
                return 0
            elif recognize_text.lower()=='open notepad':
                self.open_notepad()
                return 0
            elif recognize_text.lower()=='play music':
                self.play_music()
                return 0
            else:
                return 1
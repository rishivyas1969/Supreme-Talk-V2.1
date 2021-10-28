import speech_recognition as sr
from datetime import datetime

r = sr.Recognizer()
texts = []
adjusted = 0

def searchForPhrase(text):

    if "save me" in text:

        text = text.replace("save me", "")
        texts.append(text)

        with open("supremeText.txt", 'a') as f:
            now = datetime.now()
            f.write('\n -- ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + " --")
            for i in  texts:
                f.write("\n"+i)
            f.write("\n")
            print("-- File Saved! --\n")
        
        texts.clear()
    else:
        texts.append(text)

def adjustNoise(source):
    r.adjust_for_ambient_noise(source=source)
    adjusted=1
    print("Adjusted for noise.")

def convert(audioFile):

    try:
        with sr.AudioFile(audioFile) as source:
            if adjusted == 0:
                adjustNoise(source)

            audio = r.listen(source)

            text = r.recognize_google(audio)
            
            text = text.lower()
            searchForPhrase(text)
            if len(texts) > 10:
                texts.pop(0)

            print(text)

            
        return text

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return e
        
    except sr.UnknownValueError:
        print("unknown error occured")
        text = "[ SOME SOUNDS ]"
        texts.append(text)
        return text
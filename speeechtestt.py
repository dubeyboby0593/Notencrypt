import speech_recognition as sr

def voice_authenticate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something to authenticate:")
        audio = r.listen(source)
    
    # Recognize the voice input
    try:
        text = r.recognize_google(audio)
        if text == "authenticate":
            print("Voice authenticated!")
            return True
        else:
            print("Authentication failed!")
            return False
    except sr.UnknownValueError:
        print("Authentication failed!")
        return False
voice_authenticate()
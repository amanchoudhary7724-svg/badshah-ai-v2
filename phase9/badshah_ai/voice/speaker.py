class Speaker:
    def say(self, text):
        try:
            import pyttsx3
            e = pyttsx3.init()
            e.say(text)
            e.runAndWait()
        except Exception:
            pass

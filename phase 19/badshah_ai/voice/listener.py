class Listener:
    def __init__(self):
        self.ready = False
        try:
            import speech_recognition as sr
            self.sr = sr; self.recognizer = sr.Recognizer(); self.ready = True
        except Exception:
            self.ready = False
    def listen_once(self, timeout=5, phrase_time_limit=8) -> str:
        if not self.ready:
            print("SpeechRecognition not available."); return ""
        try:
            with self.sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            try: return self.recognizer.recognize_google(audio, language="hi-IN")
            except Exception: return self.recognizer.recognize_google(audio, language="en-IN")
        except Exception as e:
            print("Listen error:", e); return ""

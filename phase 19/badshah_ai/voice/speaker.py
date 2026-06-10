from badshah_ai.config.settings import settings
class Speaker:
    def __init__(self):
        self.engine = None
        try:
            import pyttsx3
            self.engine = pyttsx3.init()
            self.engine.setProperty("rate", settings.voice_rate)
            self.engine.setProperty("volume", settings.voice_volume)
        except Exception:
            self.engine = None
    def say(self, text: str):
        if self.engine:
            try:
                self.engine.say(str(text)); self.engine.runAndWait()
            except Exception: pass

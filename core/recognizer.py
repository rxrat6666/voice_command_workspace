import json
import vosk
from vosk import Model, KaldiRecognizer

vosk.SetLogLevel(-1) #Логи воска

MODEL_PATH = "models/vosk-model-small-ru-0.22"
SAMPLE_RATE = 16000


class SpeechRecognizer:
    def __init__(self):
        self.model = Model(MODEL_PATH)
        self.recognizer = KaldiRecognizer(self.model, SAMPLE_RATE)

    def accept_audio(self, data: bytes) -> str | None:
        if self.recognizer.AcceptWaveform(data):
            result = json.loads(self.recognizer.Result())
            text = result.get("text", "").lower().strip()
            return text if text else None
        return None


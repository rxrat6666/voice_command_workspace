import vosk
vosk.SetLogLevel(-1)

import sounddevice as sd
import queue
import json
import time
from vosk import Model, KaldiRecognizer

MODEL_PATH = "models/vosk-model-small-ru-0.22"

SAMPLE_RATE = 16000
BLOCK_SIZE = 8000


def listen_until_keywords(keywords: list[str]) -> str:
    """
    Слушает микрофон, пока не услышит ключевые слова
    """
    print("Слушаю...")

    q = queue.Queue()    

    def _callback(indata, frames, time_info, status):
        if status:
            print(status)
        q.put(bytes(indata))

    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, SAMPLE_RATE)

    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE,
        dtype="int16",
        channels=1,
        callback=_callback
    ):
        while True:
            data = q.get()

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").lower().strip()

                if not text:
                    continue

                print("✅Распознано:", text)

                for kw in keywords:
                    if kw in text:
                        print("Команда найдена:", kw)
                        return text


import sounddevice as sd
import queue
import json
import time
from vosk import Model, KaldiRecognizer

MODEL_PATH = "models/vosk-model-small-ru-0.22"
SAMPLE_RATE = 16000

q = queue.Queue()

def callback(indata, frames, time_info, status):
    q.put(bytes(indata))

print("Загрузка модели...")
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)

print("Говори (5 секунд)...")

with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback
):
    start_time = time.time()
    while time.time() - start_time < 5:
        data = q.get()
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            if text:
                print("Распознанно:", text)

print("Готово")


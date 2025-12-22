import sounddevice as sd
import numpy as np

DURATION = 3
SAMPLE_RATE = 44100

print("Говори в микрофон...")

audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
)

sd.wait()

volume = np.linalg.norm(audio)
print("Уровень звука:", volume)

if volume > 1:
    print("Микрофон РАБОТАЕТ")
else:
    print("Слишком тихо или не тот микрофон")



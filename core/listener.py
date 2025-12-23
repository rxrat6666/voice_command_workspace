import sounddevice as sd
import queue

SAMPLE_RATE = 16000
BLOCK_SIZE = 8000


class AudioListener:
    def __init__(self):
        self.q = queue.Queue()

    def _callback(self, indata, frames, time_info, status):
        if status:
            print(status)
        self.q.put(bytes(indata))

    def start(self):
        return sd.RawInputStream(
                samplerate=SAMPLE_RATE,
                blocksize=BLOCK_SIZE,
                dtype="int16",
                channels = 1,
                callback=self._callback
        )

    def get_audio(self) -> bytes:
        return self.q.get()

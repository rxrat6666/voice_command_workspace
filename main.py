from core.usb_check import is_allowed_device_connected
from core.listener import AudioListener
from core.recognizer import SpeechRecognizer
from core.commands import handle_command
from core.launcher import launch


def main():
    # 1. Проверка безопасности (USB)
    if not is_trusted_usb_connected():
        return  # тихо выходим, без логов

    # 2. Инициализация компонентов
    listener = AudioListener()
    recognizer = SpeechRecognizer()

    # 3. Запуск микрофона
    with listener.start():
        while True:
            audio_data = listener.get_audio()
            text = recognizer.accept_audio(audio_data)

            if not text:
                continue

            command = handle_command(text)
            if not command:
                continue

            launch(command)
            break  # один запуск — один workspace


if __name__ == "__main__":
    main()


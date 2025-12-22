from core.recognizer import listen_until_keywords
from core.commands import handle_command

def main():
    print("Voice Command Workspace запущен")

    #слушаем любые слова
    text = listen_until_keywords([
        "начать",
        "хочу",
        "включи",
        "работу",
        "счастья",
        "систему"
    ])

    print("Полный текст:", text)

    command = handle_command(text)

    if command == "start_workspace":
        print("Запускаем workspace")
        #позже тут будет запуск приложений
    else:
        print("команда не распознана")



if __name__ == "__main__":
    main()

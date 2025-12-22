def handle_command(text: str) -> str | None:
    text =  text.lower()

    start_keywords = [
            "начать",
            "хочу",
            "включи"
    ]

    target_keywords = [
            "работу",
            "счастья",
            "систему"
    ]

    if any(k in text for k in start_keywords) and any(t in text for t in target_keywords):
        print("WORKSPACE STARTED")
        return "start_workspace"

    return None

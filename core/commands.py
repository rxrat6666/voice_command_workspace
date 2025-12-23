from config.commands import COMMANDS

def handle_command(text: str) -> dict | None:
    text = text.lower()

    for cmd in COMMANDS:
        if any(k in text for k in cmd["start_keywords"]) and \
           any(t in text for t in cmd["target_keywords"]):
            return {
                "action": cmd["action"],
                "mode": cmd["mode"]
            }

    return None


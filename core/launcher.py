import subprocess
from config.workspaces import WORKSPACES


def launch(command: dict) -> bool:
    """
    Запускает действие на основе команды
    Возвращает True если успешно
    """
    if not command:
        return False

    if command.get("action") != "start_workspace":
        return False

    mode = command.get("mode")
    commands = WORKSPACES.get(mode)

    if not commands:
        return False

    for cmd in commands:
        try:
            subprocess.Popen(cmd.split())
        except Exception:
            return False

    return True


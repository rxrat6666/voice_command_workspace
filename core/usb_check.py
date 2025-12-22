import subprocess

#получаем список устройств
def get_usb_devices():
    result = subprocess.run(
            ['lsusb'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
    )
    return result.stdout


#Вставь ID своего телефона 
target_device = "04e8:6860"


#Получаем список устройств
devices = get_usb_devices()


#базовая проверка
if target_device in devices:
    print(f"телефон {target_device} подключен!")
else:
    print("Телефон не найден")

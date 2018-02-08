###########################
# Thibault Lebourgeois    #
# 05/02/2017              #
###########################

# IMPORTS
import socket
import base64
import sys
from threading import Thread


# CLASS TO HANDLE THREADS
class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New server started at %s:%d" % (ip, port))

    def run(self):
        while True:
            data = conn.recv(2048)
            print "[+] Server received data:", base64.b64decode(data)
            input_response = raw_input("[*] Multithreaded Python server - Enter Response from Server:")
            if input_response == 'close':
                conn.close()
                break
            conn.send(base64.b64encode(input_response))


# MAIN
if __name__ == "__main__":
    try:
        TCP_IP = '0.0.0.0'
        TCP_PORT = 443
        BUFFER_SIZE = 4096

        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.bind((TCP_IP, TCP_PORT))
        threads = []

        while True:
            tcpServer.listen(4)
            print "[*] Multithreaded server : Waiting for connections from clients..."
            (conn, (ip, port)) = tcpServer.accept()
            newthread = ClientThread(ip, port)
            newthread.start()
            threads.append(newthread)

        # close all threads
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print("Hasta la vista, BB")
        sys.exit()

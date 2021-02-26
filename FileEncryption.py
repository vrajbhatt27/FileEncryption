from cryptography.fernet import Fernet
import os


class Encryption:
    def __init__(self, key):
        self.key = key

    def encrypt_data(self, data):
        if isinstance(data, bytes):
            pass
        else:
            data = data.encode()

        f = Fernet(self.key)

        cipher = f.encrypt(data)
        return cipher

    def decrypt_data(self, data):
        f = Fernet(self.key)
        return f.decrypt(data)


try:
    os.mkdir('encFiles')
except:
    pass

try:
    os.mkdir('decFiles')
except:
    pass

path = './Files/'
path2 = './encFiles/'
path3 = './decFiles/'
folder_files = os.listdir(path)
enc_files = os.listdir(path2)

key = None


def gen_key():
    key = Fernet.generate_key()
    with open('key.pem', 'wb') as f:
        f.write(key)


def encrypt_files():

    if len(folder_files) == 0:
        print('No files present')
        return

    gen_key()

    for file in folder_files:
        with open(path+file, 'rb') as f:
            data = f.read()

        with open('key.pem', 'rb') as f:
            key = f.read()

        enc = Encryption(key)

        enc_data = enc.encrypt_data(data)

        with open(path2+(file.split('.')[0])+'.encrypted', 'wb') as f:
            f.write(enc_data)

    print('done encryption')


def decrypt_files():
    if len(enc_files) == 0:
        print('No files present')
        return

    for file in enc_files:
        with open(path2+file, 'rb') as f:
            data = f.read()

        with open('key.pem', 'rb') as f:
            key = f.read()

        enc = Encryption(key)
        org_data = enc.decrypt_data(data)

        with open(path3+(file.split('.')[0])+'.txt', 'wb') as f:
            f.write(org_data)

    print('done decryption')


ch = input('You want to encrypt(e) or decrypt(d) ? [e/d]: ')

if ch == 'e':
    encrypt_files()
elif ch == 'd':
    decrypt_files()
else:
    print('Invalid Input !!!')

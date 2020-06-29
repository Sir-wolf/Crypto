#!/usr/bin/python3
from cryptography.fernet import Fernet
import KeyManager as km
import os


def encrypt_string(message):
    f = Fernet(km.load_key())
    return f.encrypt(message)


def encrypt_file(path):
    f = Fernet(km.load_key())
    try:
        with open(path, 'rb') as file:
            print("Encrypting: " + path)
            encrypted_byes = f.encrypt(file.read())
        with open(path, 'wb') as file:
            file.write(encrypted_byes)
        return True
    except (IOError, PermissionError, FileExistsError, FileNotFoundError) as e:
        print(e)
        print("Error encrypting file: " + path)
        return False


def encrypt_path(path):
    files = get_files(path)
    for f in files:
        encrypt_file(f)


def get_files(path):
    list_of_files = os.listdir(path)
    all_files = list()
    for f in list_of_files:
        try:
            full_path = os.path.join(path, f)
            if os.path.isdir(full_path):
                all_files = all_files + get_files(full_path)
            else:
                all_files.append(full_path)
        except PermissionError:
            pass

    return all_files

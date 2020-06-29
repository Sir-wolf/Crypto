#!/usr/bin/python3
from cryptography.fernet import Fernet
import cryptography.fernet as fernet
import KeyManager as km
import os


def decrypt_string(message):
    f = Fernet(km.load_key())
    return f.decrypt(message)


def decrypt_file(path):
    f = Fernet(km.load_key())
    try:
        try:
            with open(path, 'rb') as file:
                print("Decrypting: " + path)
                decrypted_byes = f.decrypt(file.read())
            with open(path, 'wb') as file:
                file.write(decrypted_byes)
            return True
        except (IOError, PermissionError, FileExistsError, FileNotFoundError) as e:
            print(e)
            print("Error decrypting file: " + path)
            return False
    except fernet.InvalidToken:
        print("The file is not encrypted, or the key does not match.")
        return False


def decrypt_path(path):
    files = get_files(path)
    for f in files:
        print("Decrypting: " + f)
        decrypt_file(f)


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

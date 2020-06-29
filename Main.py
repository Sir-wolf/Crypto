#!/usr/bin/python3
import os
import sys


import cryptography.fernet as fernet

import Decryption as d
import Encryption as e
import KeyManager as km


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def start():
    print()
    print("Program started. Type \"quit\" at any prompt to stop.")
    if km.check_key():
        should_key = input("Should a new key be written? (Y/N) > ").lower().strip()
        if should_key == "no" or should_key == "n" or should_key == "false":
            options()
        elif should_key == "yes" or should_key == "y" or should_key == "true":
            print("IF YOU REWRITE THE KEY, ANYTHING THAT WAS ENCRYPTED WITH THE OLD KEY WILL BE IMPOSSIBLE TO DECRYPT")
            are_you_sure = input("Are you sure? (Y/N) > ").lower().strip()
            if are_you_sure == "no" or are_you_sure == "n" or are_you_sure == "false":
                print("There was no new key written.")
                options()
            elif are_you_sure == "yes" or are_you_sure == "y" or are_you_sure == "true":
                km.write_key()
                print("A new key was written...")
                options()
            elif are_you_sure == "quit" or are_you_sure == "stop":
                quit()
            else:
                print("Input not recognized... no new key was written.")
                options()
        elif should_key == "quit" or should_key == "stop":
            quit()
        else:
            print("Input not recognized.")
            start()
    else:
        sys.stdout.write("No key exists, forcing a new write... ")
        km.write_key()
        print("new key has been written.")
        options()


def options():
    task_type = input("What would you like to do? (Encrypt/Decrypt) > ").lower().strip()
    if task_type == "encrypt" or task_type == "enc":
        enc_type()
    elif task_type == "decrypt" or task_type == "dec":
        dec_type()
    elif task_type == "quit":
        quit()
    else:
        print("Input not recognized.")
        start()


def enc_type():
    task_type = input("What would you like to encrypt (Folder/File/String) > ").lower().strip()
    if task_type == "folder":
        folder_path = get_path()
        e.encrypt_path(folder_path)
        print("Complete.")
        start()
    elif task_type == "file":
        file_path = get_path()
        e.encrypt_file(file_path)
        print("Complete.")
        start()
    elif task_type == "string":
        message = input("Enter the string you would like to encrypt > ")
        print(e.encrypt_string(message.encode('utf-8')))
        start()
    elif task_type == "quit" or task_type == "stop":
        quit()
    else:
        print("Input not recognized.")
        start()


def dec_type():
    task_type = input("What would you like to decrypt (Folder/File/String) > ").lower().strip()
    if task_type == "folder":
        folder_path = get_path()
        d.decrypt_path(folder_path)
        print("Complete.")
        start()
    elif task_type == "file":
        file_path = get_path()
        d.decrypt_file(file_path)
        print("Complete.")
        start()
    elif task_type == "string":
        message = input("Enter the string you would like to decrypt > ")
        try:
            print(d.decrypt_string(message.encode('utf-8')))
        except fernet.InvalidToken:
            print("Decryption failed... is the message encrypted?")
    elif task_type == "quit" or task_type == "stop":
        quit()
    else:
        print("Input not recognized.")
        start()


def get_path():
    path = input("Enter the absolute path > ")
    if path.lower().strip() == "quit" or path.lower().strip() == "stop":
        quit()
    if os.path.exists(path):
        return path
    else:
        print("There seems to be nothing located there... try again?")
        get_path()


if __name__ == "__main__":
    start()
    input()

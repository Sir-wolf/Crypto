#!/usr/bin/python3
from cryptography.fernet import Fernet
import Main


def write_key():
    fernet_key = Fernet.generate_key()
    with open(Main.resource_path("key.key"), 'wb') as f:
        f.write(fernet_key)


def load_key():
    return open(Main.resource_path("key.key"), 'rb').read()


def check_key():
    try:
        with open(Main.resource_path("key.key"), 'r') as f:
            test_read = f.read()
        if test_read == "":
            return False
        else:
            return True
    except (IOError, PermissionError, FileNotFoundError, FileExistsError):
        return False

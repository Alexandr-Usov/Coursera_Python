"""
This module is designed to store keys.  It receives keys and values,
and saves them. When it receives the key, it prints the value to
the screen.
"""

import os
import sys
import json
import tempfile
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', dest='key')
    parser.add_argument('--val', dest='val', nargs='+')

    return parser


def add_key(name_space):
    return name_space.val


def print_key():
    read_file()


def save_file(data):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def read_file():
    try:
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        with open(storage_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        save_file(data=dict())
        read_file()


def main():
    data = read_file()
    parser = create_parser()
    name_space = parser.parse_args(sys.argv[1:])
    if name_space.val:
        data[name_space.key] = name_space.val
        save_file(data)
    else:
        try:
            print(data.get(name_space.key, 'Key not found'))
        except AttributeError:
            print("Key not found")


if __name__ == '__main__':
    main()

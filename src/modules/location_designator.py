#!/usr/bin/python
# -*- coding: utf-8 -*-

# Used to find the path to the file
from pathlib import Path

# Used to ask the user to give the directory using GUI
from tkinter import filedialog

from os.path import isfile


def default_path():
    path_to_db = Path(__file__).parent

    relative_path = '../../assets/'
    relative_path = str((path_to_db / relative_path).resolve())

    return relative_path


def file_exist(file_location):
    if isfile(file_location):
        return True

    return False


def location_file_text():
    path_to_db = Path(__file__).parent
    file_location = '../../assets/db_location.txt'
    return str((path_to_db / file_location).resolve())


def location_retrieval():
    file_location = location_file_text()
    if file_exist(file_location):
        with open(file_location, 'r') as f:
            db_path = f.read()
            f.close()
            return db_path
    else:
        path_to_db = input("Enter the path to the location where you wish to store Eisen's Database (press enter to "
                           "use default location): ")
        if len(path_to_db) != 0:
            path_to_db += r'\tickets.db'
        else:
            path_to_db = default_path() + r'\tickets.db'

        with open(file_location, 'w') as f:
            f.write(path_to_db)
            f.close()

        return path_to_db


def location_gui_retrieval():
    path = filedialog.askdirectory()
    return path


if __name__ == '__main__':
    print(location_retrieval())

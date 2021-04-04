# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from os import path

def inputFile():
    filepath = input("Enter the full path of the file to convert: ")
    verified = True
    if path.exists(filepath):
        if path.isfile(filepath):
            print("File " + str(filepath) + " is existing")
        else:
            print("File " + str(filepath) + " is NOT existing")
            verified = False
    else:
        print("Specified filepath is not existing")
        verified = False

    return filepath, verified

def main(name):
    # Ask for the full path of the file to convert.
    filepath, verification = inputFile()
    while not verification:
        filepath, verification = inputFile()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from os import path

def inputFile():
    val = input("Enter the full path of the file to convert: ")
    return val


def main(name):
    # Ask for the full path of the file to convert.
    filepath = inputFile()
    if os.path.exists(filepath):
        if os.path.isfile(filepath):
            print("File " + str(filepath) + " is existing")
        else:
            print("File " + str(filepath) + " is NOT existing")
    else:
        print("Specified filepath is not OK")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

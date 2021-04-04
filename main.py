# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from os import path
from fpdf import FPDF


def input_file():
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


def file_type(filepath):
    print("The file you entered is a ." + str(filepath.split(".")[1]) + " file.")


def create_pdf(filepath):
    i = 0   # Index to change the line with every new line of the original file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    with open(filepath, encoding='utf8') as f:  # Open the file to copy
        for line in f:  # Take a new line of the file
            pdf.cell(ln=i, h=5.0, align='L', w=0, txt=line, border=0)   # Copy the line to the created PDF file
            i = i + 1
    pdf.output(filepath.split(".")[0] + '.pdf', 'F')    # Close PDF file with the information


def main(name):
    # Ask for the full path of the file to convert.
    filepath, verification = input_file()
    while not verification:
        filepath, verification = input_file()
    # Determine the type of the file to convert
    file_type(filepath)
    # Convert the file to PDF format
    create_pdf(filepath)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

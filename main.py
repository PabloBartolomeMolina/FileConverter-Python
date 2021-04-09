# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from os import path
from fpdf import FPDF


def user_file():
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


# Line counter for the cases with several lines and files specified in default.txt
# In developement, need correctly implement an optimized logic on the main flow for this feature
def file_lines():
    line_count = 0
    paths = []
    f = open("defaults.txt", "r")
    # Count of total number of lines
    for line in f:
        print(line.rstrip("\n"))
        if line != "\n":
            line_count += 1
            paths.append(line)
    f.close()
    if line_count == 0:  # Not to be entered in normal conditions; just safety case
        print("No information available about files to read...")
        filepath, verified = user_file()  # User defined file
    elif line_count == 1:  # Not to be entered in normal conditions; just safety case
        filepath = f.readline()
        verified = True
    else:
        print("Several files indicated in defaults, please select one...")
        for line in paths:
            if line != "\n":
                print(line.rstrip("\n"))
                ans = input("Should I select this one?  (y/n)...   ")
                if ans == 'y':
                    print("OK")
                    filepath = line.rstrip("\n")
                    verified = True
                    break    # Break here, the file is already selected so no need to go through the rest.
                else:
                    print()
                    filepath = "No file selected"
                    verified = False
    return filepath, verified


def input_file():
    # Check if we use the specified file in the defaults.txt file or a new one
    if path.exists("defaults.txt"):
        ans = input("Shall I use the default file? (y/n)...   ")
        if ans == 'y':  # default file
            f = open("defaults.txt", "r")
            filepath = f.readline()
            if filepath.endswith("\n"):
                filepath, verified = file_lines()
            else:
                filepath = filepath.rstrip("\n")
                verified = True
            f.close()
        elif ans == 'n':  # new file to be defined by user input
            filepath, verified = user_file()  # User defined file
        else:
            print("I do not understand what you want to do. ")
            filepath, verified = user_file()  # User defined file
    else:
        filepath, verified = user_file()  # User defined file

    return filepath, verified


def file_type(filepath):
    print("The file you entered is a ." + str(filepath.split(".")[1]) + " file.")


def create_pdf(filepath):
    i = 0  # Index to change the line with every new line of the original file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    with open(filepath, encoding='utf8') as f:  # Open the file to copy
        for line in f:  # Take a new line of the file
            if line.startswith('#') or line.startswith('    #'):
                pdf.set_font('Arial', 'I', 11)
                pdf.set_text_color(0, 150, 125)
            elif line.startswith('def'):
                pdf.set_font('Arial', 'B', 12)
                pdf.set_text_color(255, 0, 0)
            else:
                pdf.set_font('Arial', '', 10)
                pdf.set_text_color(0, 0, 0)
            pdf.cell(ln=i, h=5.0, align='L', w=0, txt=line, border=0)  # Copy the line to the created PDF file
            i = i + 1
    pdf.output(filepath.split(".")[0] + '.pdf', 'F')  # Close PDF file with the information
    pdf.close()


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

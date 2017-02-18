from __future__ import print_function
import os


def renaming_files():
    # get the path to the files and the file names
    file_list = os.listdir("/home/koin/Desktop/HackRush/Bakley/Python/Learning/Udacity/prank")
    print(file_list)
    # get the saved path of the directory
    saved_path = os.getcwd()
    print("The saved path is,", saved_path)
    os.chdir("/home/koin/Desktop/HackRush/Bakley/Python/Learning/Udacity/prank")

    # rename files
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))


renaming_files()

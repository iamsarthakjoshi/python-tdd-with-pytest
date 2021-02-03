import os

def readFromFile(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError()
    file = open(filename, "r")
    line = file.readline()
    return line
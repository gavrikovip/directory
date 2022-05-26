from exportFile import recordData
from inputData import inputPeople
from importFile import importData
from check import checkFile
from ui import present

def input():
    return inputPeople()

def clickExport():
    checkFile()
    res = inputPeople()
    recordData(res)


def clickImport():
    importData()


def run():
    res = int(present())
    if res == 1:
        clickExport()
    if res == 2:
        clickImport()

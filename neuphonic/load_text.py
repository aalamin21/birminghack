import csv

def text():
    with open("../LLM/outputs.txt") as file:
        return file.readlines()[-1]
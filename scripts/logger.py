import time
import os
from datetime import datetime

file = '../data/log'

def fswitch(x):
    return {
        0: "  INFO   ",
        1: "  DEBUG  ",
        2: "  ERROR  "
    }[x]

def log(message, type=0):
    date = str(datetime.now())
    t = str.split(date, '.')
    string = '[' + fswitch(type) + ']' + " - " + t[0] + " - " + message + '\n'
    with open(file, 'a+') as f:
        f.write(string)

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#

def checkHashCode(hashCode, auth_hash):
    return hashCode == auth_hash

def getHashCode(password, p=131, M=10**9 + 7):
    hashValue = 0
    for letter in password:
        hashValue = (hashValue * p + ord(letter)) % M
    return hashValue

def authEvents(events):
    password = ''
    hashCode = 0
    result_array = []
    for event in events:
        if event[0] == 'setPassword':
            password = event[1]
            hashCode = getHashCode(password)
        elif event[0] == 'authorize':
            auth_hash = int(event[1])
            if auth_hash == hashCode:
                result_array.append(1)
            else:
                authorized = False
                # Check hash with one additional character appended
                for i in range(32, 127):  # covering printable ASCII range
                    appended_hash = (hashCode * 131 + i) % (10**9 + 7)
                    if appended_hash == auth_hash:
                        authorized = True
                        break
                result_array.append(1 if authorized else 0)
    return result_array
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#!/usr/bin/env python

import string

modulo = 41
char_map = list(string.ascii_uppercase + string.digits + '_')
file_name = 'message.txt'

def readFile(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
        message_list = content.split()
        return message_list

def modInverse(a, m):
    result = pow(a, -1, m)
    return result

def printFlag():
    flag_string = ''
    char_list = readFile(file_name)
    for item in char_list:
        mod_result = modInverse(int(item), modulo)
        flag_string += char_map[mod_result-1]

    print("picoCTF{" + flag_string + '}')

if __name__ == "__main__":
   printFlag()
#!/usr/bin/env python

import string

modulo = 37
char_list = list(string.ascii_uppercase + string.digits + '_')
flag_string = ''

f = open('message.txt', 'r')
content = f.read()
f.close()

message_list = content.split()

for item in message_list:
    mod_result = int(item) % modulo
    flag_string += char_list[mod_result]

print("picoCTF{" + flag_string + '}')
# basic-mod2

## Description

A new modular challenge! Download the message [here](https://artifacts.picoctf.net/c/500/message.txt). Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Getting Started

To begin with we'll download the file and start constructing some python to "decrypt" the file

### Download the file

We'll firstly wget the file message.txt as supplied by the task `wget https://artifacts.picoctf.net/c/500/message.txt`
```
$ wget https://artifacts.picoctf.net/c/500/message.txt
--2022-04-06 23:20:17--  https://artifacts.picoctf.net/c/500/message.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 99.86.113.27, 99.86.113.14, 99.86.113.19, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|99.86.113.27|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 85 [application/octet-stream]
Saving to: ‘message.txt’

message.txt                            100%[============================================================================>]      85  --.-KB/s    in 0s      

2022-04-06 23:20:18 (90.1 MB/s) - ‘message.txt’ saved [85/85]
```

### Construct the python

We start out by constructing the basics, improving on what we've already done for basic-mod1. We'll define functions as we go and try to parameterise where we can incase we need to reuse this code again for another task. We'll also use best practice for the [main section](https://docs.python.org/3/library/__main__.html) of the code, python advises to be "explicit over implicit"
```python
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

if __name__ == "__main__":
   char_list = readFile(file_name)
   print(char_list)
```
```
['104', '85', '69', '354', '344', '50', '149', '65', '187', '420', '77', '127', '385', '318', '133', '72', '206', '236', '206', '83', '342', '206', '370']
[Finished in 37ms]
```

So we've update the modulus number, created a `file_name` to define which file to read and created a function `readFile` this returns char_list of numbers that we will need to find the modular inverse for and map to our character map. Lets create a new function `modInverse` in python theres a built in function [pow](https://docs.python.org/3/library/functions.html#pow). We'll define two inputs to the code `a` which will be our base number or the number to work on and `m` for modulus. The exp portion of function will always be `-1` so is hardcoded as this provides the inverse of mod. Note you need Python 3.8 and above for this to work *"Changed in version 3.8: For int operands, the three-argument form of pow now allows the second argument to be negative, permitting computation of modular inverses"*

We'll also create a new printFlag function call these two other functions and print out the results.
```python
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
    char_list = readFile(file_name)
    for item in char_list:
        mod_result = modInverse(int(item), modulo)
        print(mod_result)
        

if __name__ == "__main__":
   printFlag()
```
```
28
14
22
30
18
32
30
12
25
37
8
31
18
4
37
4
1
4
1
1
3
1
1
[Finished in 42ms]
```
We see that the results returned are between 1 and 37 as defined in the character map at the beginning of the task.

Now we use the same technique as basic-mod1 to map the characters to the value using indexes, however there is 1 subtle change.

```python
def printFlag():
    flag_string = ''
    char_list = readFile(file_name)
    for item in char_list:
        mod_result = modInverse(int(item), modulo)
        flag_string += char_map[mod_result]
        
    print("picoCTF{" + flag_string + '}')
```
Running this we get list index out of range
```python
Traceback (most recent call last):
  File "/home/jimjamg/picoctf2022/cryptography/basic-mod2/basic_mod2.py", line 29, in <module>
    printFlag()
  File "/home/jimjamg/picoctf2022/cryptography/basic-mod2/basic_mod2.py", line 24, in printFlag
    flag_string += char_map[mod_result]
IndexError: list index out of range
[Finished in 32ms with exit code 1]
```
This is because our character map is no longer 0-36 but 1-37, theres a couple of ways we could solve this but the easiest for me was to subtract 1 from the mod_result.

```python
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
```
And its solved.
```
picoCTF{1NV3R53LY_H4RD_DADAACAA}
[Finished in 30ms]
```
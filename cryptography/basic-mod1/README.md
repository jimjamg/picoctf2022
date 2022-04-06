# basic-mod1

## Description

We found this weird message being passed around on the servers, we think we have a working decrpytion scheme. Download the message [here](https://artifacts.picoctf.net/c/394/message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Getting Started

To begin with we'll download the file and start constructing some python to "decrypt" the file

### Download the file

We'll firstly wget the file message.txt as supplied by the task `wget https://artifacts.picoctf.net/c/394/message.txt`
```
--2022-04-06 22:34:30--  https://artifacts.picoctf.net/c/394/message.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 143.204.199.11, 143.204.199.115, 143.204.199.13, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|143.204.199.11|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 86 [application/octet-stream]
Saving to: ‘message.txt’

message.txt                            100%[============================================================================>]      86  --.-KB/s    in 0s      

2022-04-06 22:34:30 (82.0 MB/s) - ‘message.txt’ saved [86/86]
```

### Construct the python

We start out by constructing the basics, add the shebang, a variable for the modulus number and reading in the message.txt and printing out the contents
```python
#!/usr/bin/env python

modulo = 37

f = open('message.txt', 'r')
content = f.read()
f.close()

print(content)
```
```
202 137 390 235 114 369 198 110 350 396 390 383 225 258 38 291 75 324 401 142 288 397 
[Finished in 34ms]
```
Perfect thats the basics taken care of, note I probably should of used with open but I didn't in this case, you'll see the "better" way to handle opening an closing a file in the next basic-mod2 writeup.

Next we want to split the contents of the file so that we can iterate over each value, simply we add the [.split method](https://docs.python.org/3/library/stdtypes.html#str.split) to the print `print(content.split())`
```
['202', '137', '390', '235', '114', '369', '198', '110', '350', '396', '390', '383', '225', '258', '38', '291', '75', '324', '401', '142', '288', '397']
[Finished in 28ms]
```
We now have a [list](https://docs.python.org/3/tutorial/datastructures.html) defined denoted by the [] and comma separated strings within.

Next we want to iterate over this list item by item and perform modulus (divide and get the remainder) on each value. In python we can do this by using a [for loop](https://docs.python.org/3/tutorial/controlflow.html#for-statements) `for item in variable`

```python
message_list = content.split()

for item in message_list:
    mod_result = int(item) % modulo
    print(mod_result)
```
```
17
26
20
13
3
36
13
36
17
26
20
13
3
36
1
32
1
28
31
31
29
27
[Finished in 35ms]
```
Now we have our values which need to map as defined, *"0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore"* For this i thought lets create another list(array) where we use the number as the index to retrieve. Python indexing starts at 0 so our first value would be 'A', we could do this by manually defining the array, but why do that when there are modules that already exist to do this. We're going to use the [strings](https://docs.python.org/3/library/string.html) module.

We need to add to the top of file the import for this library `import string` we can then make use of `string.ascii_uppercase` `string.digits` and finally `_` concatenating them all together as a list stored as char_list. We'll print out each value and add it to a new variable `flag_string`. We need to make sure the variable is defined before we start adding to it or we'll get an error
```python
Traceback (most recent call last):
  File "/home/jimjamg/picoctf2022/cryptography/basic-mod1/basic-mod1.py", line 17, in <module>
    flag_string += char_list[mod_result]
NameError: name 'flag_string' is not defined
[Finished in 41ms with exit code 1]
```

```python
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
    print(flag_string)
```
```
R
R0
R0U
R0UN
R0UND
R0UND_
R0UND_N
R0UND_N_
R0UND_N_R
R0UND_N_R0
R0UND_N_R0U
R0UND_N_R0UN
R0UND_N_R0UND
R0UND_N_R0UND_
R0UND_N_R0UND_B
R0UND_N_R0UND_B6
R0UND_N_R0UND_B6B
R0UND_N_R0UND_B6B2
R0UND_N_R0UND_B6B25
R0UND_N_R0UND_B6B255
R0UND_N_R0UND_B6B2553
R0UND_N_R0UND_B6B25531
```
We can now see the string is being built incrementally on each loop of the list. We'll get rid of the print after each iteration and print the `flag_string` with the `picoCTF{}` notation.

```python
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
```
```
picoCTF{R0UND_N_R0UND_B6B25531}
[Finished in 28ms]
```
Success.
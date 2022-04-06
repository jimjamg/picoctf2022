# patchme.py

## Description

Can you get the flag?

Run this [Python program](https://artifacts.picoctf.net/c/387/patchme.flag.py) in the same directory as this encrypted flag.

## Getting Started

In order to do this challenge we need to download the program and the encrypted flag.

### Download the files

We'll use wget to download files to our local machine

```
$ wget https://artifacts.picoctf.net/c/387/patchme.flag.py                                               
--2022-04-07 00:23:17--  https://artifacts.picoctf.net/c/387/patchme.flag.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 143.204.199.13, 143.204.199.77, 143.204.199.115, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|143.204.199.13|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 980 [application/octet-stream]
Saving to: ‘patchme.flag.py’

patchme.flag.py                        100%[============================================================================>]     980  --.-KB/s    in 0s      

2022-04-07 00:23:18 (11.3 MB/s) - ‘patchme.flag.py’ saved [980/980]
```
```
wget https://artifacts.picoctf.net/c/387/flag.txt.enc   
--2022-04-07 00:24:01--  https://artifacts.picoctf.net/c/387/flag.txt.enc
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 143.204.199.11, 143.204.199.115, 143.204.199.77, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|143.204.199.11|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 36 [application/octet-stream]
Saving to: ‘flag.txt.enc’

flag.txt.enc                           100%[============================================================================>]      36  --.-KB/s    in 0s      

2022-04-07 00:24:02 (22.9 MB/s) - ‘flag.txt.enc’ saved [36/36]

```

### Run the script

If we run the script we must enter a correct password for a flag, if we don't enter the correct password the flag is not displayed.

```
Please enter correct password for flag: testing
That password is incorrect
```
Looks like we'll need to take a look at the source code to see if there are any hints in there.

### View the source code

Lets open the source code
```python
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################


flag_enc = open('flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()
```
We can see the function `level_1_pw_check` is being called.

The first thing this does is collect user input for the password and store in a variable `user_pw`

Next an if statement is performed to compare `user_pw` with a concatenation of multiple strings and the use of line continuation/[explicit line joining](https://docs.python.org/3/reference/lexical_analysis.html#explicit-line-joining) using `\`

If we join this string up we get that `user_pw == "ak98-=90adfjhgj321sleuth9000"`

Bingo!
```
Please enter correct password for flag: ak98-=90adfjhgj321sleuth9000
Welcome back... your flag, user:
picoCTF{p47ch1ng_l1f3_h4ck_f01eabfa}
```

## Authors

jimjamg
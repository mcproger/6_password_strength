# Password Strength Calculator

This script shows strength of the password that user entered in range from 1 to 10 points: 

* 1 point for any digit in your password 
* 2 points for special symbols in your password like '@#$'
* 2 points for use of registers 
* 4 points if user's password not in blacklist of passwords
 
# Using

For checking password you should have file with blacklist of passwords in your repository. You can take it [here](https://github.com/danielmiessler/SecLists/tree/master/Passwords)
 
```#!bash

$ python3 password_strength.py
  Please, enter your password:
  <user password>
  Strength of your password: 1-10

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

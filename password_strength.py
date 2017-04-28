from getpass import getpass
import os 


def load_blacklist(filename='Blacklist.txt'):
    if not os.path.exists('Blacklist.txt'):
        return False
	with open(filename, mode='r', encoding='utf-8') as password_blacklist:
		passwords_blacklist = password_blacklist.read()
		return passwords_blacklist
	

def check_password_blacklist(user_password):
    if load_blacklist():
        passwords_blacklist = load_blacklist().split()
        for password in passwords_blacklist:
            if user_password in password:
	        return False
	    return True


def check_register(user_password):
    for symbol in user_password:
        if symbol.isupper():
            return True
    

def check_special_symbols(user_password):
    special_symbols = '!@#$%^&*()_='
    for symbol in user_password:
        if symbol in special_symbols:
            return True
    

def check_digit(user_password):
    digits = '0123456789'
    for symbol in user_password:
        if symbol in digits:
            return True
    

def get_password_strength(user_password):
    password_strength = 1
    summary_strength = [
    {'check': check_digit(user_password), 'strength_point': 1},
    {'check': check_special_symbols(user_password), 'strength_point': 2},
    {'check': check_register(user_password), 'strength_point': 3},
    {'check': check_password_blacklist(user_password), 'strength_point': 4}]
    for points in summary_strength:
    	if points['check']:
            password_strength += points['strength_point']
    return password_strength


if __name__ == '__main__':
    if not os.path.exists('Blacklist.txt'):
    	print('No Blacklist.txt file in current directory')
    user_password = getpass('Please, enter you password: ')
    if len(user_password) >= 6:
        print('Strength of your password: %s' % get_password_strength(user_password))
    else:
        print("Your password is too short. Minimal length of password is 6 symbols")

from getpass import getpass
import os, json, string


def load_blacklist(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, mode='r', encoding='utf-8') as password_blacklist:
        passwords_blacklist = password_blacklist.read()
        return passwords_blacklist
	

def check_password_blacklist(user_password, filepath):
    if load_blacklist(filepath):
        passwords_blacklist = load_blacklist(filepath).split()
        for password in passwords_blacklist:
            if user_password == password:
                return False
        return True


def check_register(user_password):
    for symbol in user_password:
        return bool(symbol.isupper())
    

def check_special_symbols(user_password):
    for symbol in user_password:
        if symbol in string.punctuation:
            return True
    

def check_digit(user_password):
    for symbol in user_password:
        if symbol in string.digits:
            return True
    

def make_summary_strength_check(user_password, filepath):
    summary_strength_check = [
	{'check': check_password_blacklist(user_password, filepath), 'strength_point': 4},
	{'check': check_special_symbols(user_password), 'strength_point': 2},
    {'check': check_register(user_password), 'strength_point': 2},
    {'check': check_digit(user_password), 'strength_point': 1}]
	return summary_strength_check


def get_password_strength(user_password, filepath):
    password_strength = 1
    summary_strength_check = make_summary_strength_check(user_password, filepath)
    for points in summary_strength_check:
    	if points['check']:
            password_strength += points['strength_point']
    return password_strength


if __name__ == '__main__':
    filepath = input('Please, enter path to password\'s Blacklist file: ')
    user_password = getpass('Please, enter you password: ')
    if len(user_password) >= 6:
        print('Strength of your password: %s' % get_password_strength(user_password, filepath))
    else:
        print("Your password is too short. Minimal length of password is 6 symbols")

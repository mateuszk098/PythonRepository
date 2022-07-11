# Python ma specjalna biblioteke getpass
from getpass import getpass

login = input('Enter login: ')
# Wpisywanie hasla bedzie niewidoczne
password = getpass('Enter password: ')

print('Loggin in...')

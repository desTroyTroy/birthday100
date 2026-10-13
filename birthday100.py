
'''Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they 
will turn 100 years old.
import time'''

import time

name = input('Enter your name: ')
age = int(input('Enter your age: '))
msgQty = int(input('How many time would you like to repeat the answer?: '))
birthday100 = 100 - age + int(time.strftime('%Y'))
print(f'{name.strip()}, your 100th birthday is in the year {birthday100}\n'*msgQty)
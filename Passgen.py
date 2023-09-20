import secrets
import random
import string

while True:
    
    length = 0
    print('Please choose how long you would like your password to be')
    length = int(input())

    if length >0:
            password= ("".join([secrets.choice(string.digits + string.ascii_letters + string.punctuation) for i in range(length)]))
            print("\n"+"Here is your password: " "\n" + str(password))
            break
    else:
        continue

import random
import string

pass_len = input("1-100 Characters Length: ")

for _ in range(1, int(pass_len)):
    print(random.choice(''.join([string.ascii_letters, string.digits])), end='')

dont_exit = input() # To avoid force close on cmd
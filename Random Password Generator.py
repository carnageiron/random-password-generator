import string
import random

# initializing size of string
N=int(input("Enter the length of the password:"))

# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_uppercase +
							string.digits, k=N))

# print result
print("The generated random string : " + str(res))

#program to generate strong random passwords
import random 
import string 

pass_length = int(input('Enter length of password you want: '))

allchar = string.ascii_letters + string.digits + string.punctuation 
password = ""
for i in range(pass_length):
    password += random.choice(allchar)

print("Generated random password is :" , password)
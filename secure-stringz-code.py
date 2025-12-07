import random
import string
length = int(input("Enter the length of the password you want: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ""
for item in range(length):
    c = random.choice(characters)
    password += c
print("Your password is: ",password)
strength = 0

if any(char.isupper() for char in password):
    strength += 1
if any(char.islower() for char in password):
    strength += 1
if any(char.isdigit() for char in password):
    strength += 1
if any(char in string.punctuation for char in password):
    strength += 1
if len(password) >= 12:
    strength += 1

# Now check strength score
if strength <= 2:
    print("Weak password")
elif strength == 3 or strength == 4:
    print("Medium password")
else:
    print("Strong password")

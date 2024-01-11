import random
import string

"To Generate a Password"
def get_password_generator(lengthOfInput):
    characters = string.ascii_letters + string.digits + string.punctuation
    if lengthOfInput <= 12:
        password = ''.join(random.choice(characters) for _ in range(lengthOfInput))
    return password

lengthOftheInput = int(input())
    
def main():
    try:
        if lengthOftheInput <= 0:
            raise ValueError
    except ValueError:
        print("Invalid password length")
    exit()

get_password = get_password_generator(lengthOftheInput)

print("******Password Generator*******")
print("Letters and digits and punctuation contains in the Password field")
print()
print("Generated Password: " + get_password)
main()

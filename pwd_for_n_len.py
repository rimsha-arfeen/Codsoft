import string
import random
all_characters=string.ascii_letters+string.digits+string.punctuation
length=int(input("Enter the desired length for your password:"))
password = ''.join(random.choices(all_characters, k=length))
print("Your desired length password is:",password)
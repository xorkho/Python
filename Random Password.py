import random
import string
password_length=8
password_generates=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(password_length):
    password+=random.choice(password_generates)
print(f"Your Generated password is:{password}")
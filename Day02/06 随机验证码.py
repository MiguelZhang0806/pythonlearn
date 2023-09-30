import random
import string


s = ""
for i in range(5):
    all_chars = string.ascii_lowercase + string.ascii_uppercase +string.digits
    random_char = random.choice(all_chars)
    s += random_char

print(s)


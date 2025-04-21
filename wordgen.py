import random
import string

def generate_word():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

while True:
    print(generate_word())

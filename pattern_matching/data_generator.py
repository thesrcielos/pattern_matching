import random
import string
from pattern_matching import constants

def generate_patterns_data(size, pattern_probability=0.2):
    pattern_size = random.randint(0, size//15)
    chars = string.ascii_uppercase 
    pattern = ""

    for _ in range(pattern_size):
        pattern += random.choice(chars)

    data = []
    i = 0

    while i < size:
        if random.random() < pattern_probability and i + len(pattern) <= size:
            data.append(pattern)  
            i += len(pattern)
        else:
            data.append(random.choice(chars))  
            i += 1

    data = "".join(data)
    return (data, pattern)

def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)

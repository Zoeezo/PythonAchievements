import random

def shuffle(word):
    randomised = ''.join(random.sample(word, len(word)))

    return randomised

print(shuffle('Hoii'))
print(shuffle('Superheld'))
print(shuffle('Hackermen'))
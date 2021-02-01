import random
def randInt (min=0, max=100):
    num = random.random()*(max-min) + min
    numer = round(num)
    return numer
print(randInt())
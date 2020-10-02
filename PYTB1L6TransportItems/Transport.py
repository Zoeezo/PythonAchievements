import os
import time
import random

factory = []
distribution = []
shop = []
product = 'Laptop'

def display():
    time.sleep(1)
    os.system('cls')
    print('Factory:', factory)
    print('Distribution: ', distribution)
    print('Shop: ', shop)

def main():
    global factory
    global distribution
    global shop

    display()

    factory.append(product)

    display()

    temp = factory.pop(factory.index(product))

    distribution.append(temp)

    display()

    temp = distribution.pop(distribution.index(product))

    shop.append(temp)

    display()

    if(random.randint(1, 2) == 2):
        shop.pop(0)

while True:
    main()
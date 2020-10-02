import time
import sys

def Calling(name, number):
    print('&: Hallo!')
    time.sleep(1)
    print('#: Hallo! Wie ben jij?')
    time.sleep(1)
    print('&: Ik ben ' + name + '!')
    time.sleep(1)
    print('#: Ohh hallo, ' + name + ', ik ben best druk nu. Kan ik je later terugbellen?')
    time.sleep(1)
    print('&: Ja hoor, mijn nummer is: ' + str(number))
    time.sleep(1)
    print('#: Okii, dagg!')
    time.sleep(1)
    print('&: Tot later!')

Calling(sys.argv[1], sys.argv[2])
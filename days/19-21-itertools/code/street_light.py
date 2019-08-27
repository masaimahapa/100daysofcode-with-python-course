from itertools import cycle
import time
import os

lights= cycle(['green', 'orange', 'red'])

# press control +c to stop running the infinite loop below 
while True:
    os.system('clear')
    colour= next(lights)
    if colour== 'green' or colour=='red':
        print(colour)
        time.sleep(5)
    elif colour== 'orange':
        print(colour)
        time.sleep(2)


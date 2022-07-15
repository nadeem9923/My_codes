# Program  to implement generator function to display square of numbers from 1 to 10. 

import math

def square():
    for x in range(1,11):
        yield (x*x)


for val in square():
    print(val)
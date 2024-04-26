import numpy as np
import math as m

def gen():
    balls = []
    numbers = [1,2,3,4,5,6]
    n=6
    for i in range(4):
        index_random = np.random.randint(n, size=1)
        balls.append(numbers[int(index_random)])
        numbers.pop(int(index_random))
        n += -1
    return balls
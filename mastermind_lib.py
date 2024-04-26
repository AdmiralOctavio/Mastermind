import numpy as np
import math as m

#generates non conscecutive random 4 digit number
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

#converts values of list to integers
def toInt(list):
    for i in range(len(list)):
        list[i] = int(list[i])
    return list

#converts list to a single string
def toStr(list):
    string = ""
    for i in range(len(list)):
        string += str(list[i])
    return string
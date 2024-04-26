import numpy as np
import math as m

def gen():
    balls = []
    for i in range(0,4):
        num = str(np.random.randint(6, size=1)+1)
        balls.append(num[1])
    return balls

def UI():
    row = ["- "]*7
    rowStr = ""
    column = ["|"] + ["  "]*5 + ["|"]
    columnStr = ""
    for i in range(0,6): rowStr += row[i]
    for i in range(0,7): columnStr += column[i]
    print(rowStr)
    for i in range(0,6): print(columnStr)
    print(rowStr)

def inpput():
    answer = input("Input answer: ").replace(" ","")
    ans = []
    if len(answer) > 4:
        print("Please submit a four digit number ")
        answer = input("Input answer: ").replace(" ", "")
    else:
        for i in range(0,4): ans.append(answer[i])
    return ans
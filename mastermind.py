import math
import numpy as np
import mastermind_gen as m

balls = m.gen()

def UIStartup():
    global columnStr
    global rowStr
    row = ["- "]*7
    rowStr = ""
    column = ["|"] + ["  "]*5 + ["|"]
    columnStr = ""
    for i in range(0,6): rowStr += row[i]
    for i in range(0,7): columnStr += column[i]
    print("Welcome to Mastermind! The rules are as such: \n 1) You have 10 attempts to guess the correct combination 2) You may only enter numbers ranging from 1 to 6 \n 3) X signifies the number is incorrect, 0 indicates your number is present but incorrectly placed. # indicates the number is present and correctly placed.")

def inpput():
    answer = input("Input answer: ").replace(" ","")
    ans = []

    if len(answer) > 4:

        print("Please submit a four digit number ")
        answer = input("Input answer: ").replace(" ", "")

    else: ans += [answer[i] for i in range(4)]

    return ans

def game():
    global correctFactor
    TF = []
    attempts = 0
    #Reads better than a for loop
    while attempts < 10:
        ans = inpput()
        FullC = 0
        HalfC = 0
        Inc = 0
        for i in range(0,4):
            correctFactor = 0
            if ans[i] in balls:
                if ans[i] == balls[i]:
                    FullC += 1
                    correctFactor += 1
                else: HalfC += 1
            else: Inc += 1
        TF.append("#"*FullC + "0"*HalfC + "X"*Inc)
        attempts += 1
        print(TF)
        print(balls)
        print(ans)
        if correctFactor == 4:
            attempts = 10
            win()

def win():
    yes = ["yes", "y", "ye", "yuh", "ya"]
    repeat = input("Congratulations, you have won! Would you like to play again?")
    if repeat.lower() in yes:
        correctFactor = 0
        game()
    else:
        exit()

game()

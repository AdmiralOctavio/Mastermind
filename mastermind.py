import math
import numpy as np
import mastermind_lib as m

yes = ["yes", "y", "ye", "yuh", "ya"]

def UIStartup():
    print("\n Welcome to Mastermind! Here are the rules: \n 1) You have 10 attempts to guess the correct combination \n 2) You may only enter numbers ranging from 1 to 6 \n 3) X signifies the number is incorrect, 0 indicates your number is present but incorrectly placed. # indicates the number is present and correctly placed.")

def inpput():
    answer = input("Input answer: ").replace(" ","")
    ans = []
    if len(answer) > 4:
        print("Please submit a four digit number ")
        answer = input("Input answer: ").replace(" ", "")
    else: ans += [answer[i] for i in range(4)]
    return m.toInt(ans)

def game():
    global correctFactor
    global TF
    global ans
    global screen
    global balls
    balls = m.gen()
    screen = []
    TF = []
    attempts = 0
    #Reads better than a for loop
    while attempts < 11:
        ans = inpput()
        correctFactor = 0
        FullC = 0
        HalfC = 0
        Inc = 0
        for i in range(0,4):
            if int(ans[i]) in balls:
                if int(ans[i]) == balls[i]:
                    FullC += 1
                    correctFactor += 1  
                else: HalfC += 1
            else: Inc += 1
        TF.append("#"*FullC + "0"*HalfC + "X"*Inc)
        attempts += 1
        if correctFactor == 4:
            attempts = 11
            win()
        if attempts == 10: lose()
        print(attempts)
        UI(attempts-1)

def UI(iteration):
    print("\n")
    screen.append(m.toStr(ans) + " | " + m.toStr(TF[iteration])+ "\n")
    print(m.toStr(screen))

def win():
    repeat = input("Congratulations, you have won! Would you like to play again? ")
    if repeat.lower() in yes: main()
    else: exit()

def lose():
    repeat = input("You have lost. Would you like to play again? ")
    if repeat.lower() in yes: main()
    else: exit()

def main():
    UIStartup()
    game()
main()
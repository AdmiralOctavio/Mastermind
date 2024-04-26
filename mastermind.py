import mastermind_lib as m
yes = ["yes", "y", "ye", "yuh", "ya"]
def inpput():
    answer, ans = input("Input answer: ").replace(" ",""), []
    if len(answer) > 4 or answer.isdigit() == False:
        print("Please submit a four digit number ")
        answer = input("Input answer: ").replace(" ", "")
    else: ans += [answer[i] for i in range(4)]
    return m.toInt(ans)
def game():
    global TF, ans, screen, balls, correctFactor
    screen, TF, attempts, balls = [], [], 0, m.gen()
    while attempts < 11:
        ans = inpput()
        FullC, HalfC, Inc, correctFactor = 0, 0, 0, 0
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
            win()
            break
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
    print("\n Welcome to Mastermind! Here are the rules: \n 1) You have 10 attempts to guess the correct combination \n 2) You may only enter numbers ranging from 1 to 6 \n 3) X signifies the number is incorrect, 0 indicates your number is present but incorrectly placed. # indicates the number is present and correctly placed.")
    game()
main()
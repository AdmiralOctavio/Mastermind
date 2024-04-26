import math
import numpy as np
import mastermind_gen as m

balls = m.gen()

def game():
    TF = []
    ans = m.inpput()
    for i in range(0,4):
        if ans[i] in balls:
            if ans[i] == balls[i]:
                TF.append("#")
            else:
                TF.append("0")
        else:
            TF.append("X")
    print(TF)
    print(balls)
    print(ans)
game()

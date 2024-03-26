#剪刀石头布游戏，连续游戏，先赢得3局者胜利。
import random

robWinCount = 0
youWinCount = 0

print("\n ---WELCOME 2 SCISSOR GAME")

while True:
    robShow = random.choice(['S', 'R', 'P']) #在序列中随机选一个
    #print(robShow)

    youShow = input("input (S)cissor/(R)ock/(R)aper:").upper()

    if youShow not in ['S', 'R', 'P']:
        print("WRONG INPUT!!!")
        continue

    #if(youShow == robShow):
    if youShow == robShow:
        print("The same, game goes on")
    #elif((youShow == 'S' and robShow == 'R') or (youShow == 'R' and robShow == 'P') or (youShow == 'P' and robShow == 'S')):
    elif (youShow, robShow) in  [('S', 'R'), ('R', 'P'), ('P', 'S')]:  # 使用元组解包简化判断  
        #robWinCount = robWinCount + 1
        robWinCount += 1
        #print("YOU LOSE..  | YOU:" + youShow + ",ROB:" + robShow + " | TOTAL(YOU:ROB):" + str(youWinCount) + ":" + str(robWinCount) )
        print(f"YOU LOSE.. YOU:{youShow},ROB: {robShow} | TOTAL(YOU:ROB):{youWinCount}:{robWinCount}")  
    else:
        #youWinCount = youWinCount + 1
        #print("YOU WIN!  | YOU:" + youShow + ",ROB:" + robShow + " | TOTAL(YOU:ROB):" + str(youWinCount) + ":" + str(robWinCount) )
        youWinCount += 1
        print(f"YOU WIN!  | YOU:{youShow},ROB:{robShow} | TOTAL(YOU:ROB):{youWinCount}:{robWinCount}")

    if youWinCount == 3:
        print("YOU ARE THE WINNER!!!!!!GAME OVER")
        break
    elif robWinCount == 3:
        print("YOU LOOSE THE WINNER!!!!!!GAME OVER")
        break
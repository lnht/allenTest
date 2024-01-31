##print("Guess number，input：")
##temp = input()
## 一共5次机会，如果猜对了，跳出，否则告知大了或者小了。如果达到5次还没猜中，结束
import random


counter = 5
#rightNum = random.choice([2,4,6,8,10]) #在序列中随机选一个
rightNum = random.randint(1, 20) #在【1, 10】整数中随机选一个

temp = print("\n ---WELCOME! THIS IS GUESS NUMBER GAME(1-20，5chances)---\n")

while(counter > 0):
    #print("Guess(" + counter + "/5):  ")
    temp = input("Guess(" + str(counter) + "/5times):  ")
    guessNum = int(temp)
    counter = counter - 1

    if (guessNum == rightNum):
        print("YOU WIN!")
        break
    else:
        if(guessNum > rightNum):
            print("Too big, try again!")
        else:
            print("Too small,try again!")
    if(counter == rightNum):
        print("------GAME OVER-----")

        
        

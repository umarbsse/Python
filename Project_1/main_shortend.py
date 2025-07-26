import random
import sys
'''
1 for snake
-1 for water
0 for gun
'''

computer =  random.choice([-1,0,1])
youstr = input("Enter your choice from s,w,g: ")
if(youstr=="w" or youstr=="s" or youstr=="g"):
    print("string game...")
else:
    print("Someting went wrong")
    sys.exit()  # Program stops here
youDict = {"s": 1, "w":-1, "g":0}
reverseDict = {1:"Snake", -1:"Water",0:"Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]} = Computer chose {reverseDict[computer]}")

if(computer==you):
    print("Its Draw")
else:
    if( (computer-you)==-1 or (computer-you)==2 ):
        print("You Lose!")
    else:
        print("You Win!")
import random

print("computer turn : Stone(s) paper (p)  Scissors(c)  ?")
randomNo = random.randint(1,3)

if randomNo==1:
    computer='s'
elif randomNo==2:
    computer='p'
elif randomNo==3:
    computer='c'

you = input("your turn : Stone(s)  Paper(p) or Scissors(c) ?")

def gameresult(computer ,you):
    if computer==you:
        return None
    elif computer=='s':
        if you=='p':
            return False
        elif you=='c':
            return True
    elif computer=='p':
        if you=='c':
            return False
        elif you=='s':
            return True
    elif computer=='c':
        if you=='s':
            return False
        elif you=='p':
            return True
              
if randomNo==1:
    computer ='s'
elif randomNo==2:
    computer ='p'
elif randomNo==3:
    computer ='c'

a = gameresult(computer,you)
print(f"computer chose {computer}")
print(f"you chose {you}")

if a== None :
    print("the game is tie")
elif a:
    print("you winnnnnnnn")
else:
    print("you lose !  Better lucj next time")
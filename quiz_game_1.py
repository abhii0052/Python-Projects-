print("Welcome to my computer Quiz Game !")

playing = input("Do you Want to Play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

answer=input("What does CPU stand for ? ")
if answer.lower() =="central processing unit" :
    print("Correct ")
    score += 1
else:
    print("Incorrect ! ")
    print("Incorrect ! ")



answer=input("What does GPU stand for ? ")
if answer.lower() =="graphics processing unit" :
    print("Correct ")
    score += 1
else:
    print("Incorrect ! ")
    print("Incorrect ! ")



answer=input("What does RAM stand for ? ")
if answer.lower() =="random access memory" :
    print("Correct ")
    score += 1
else:
    print("Incorrect ! ")
    print("Incorrect ! ")

answer=input("What does PSU stand for ? ")
if answer.lower() =="power supply unit":
    print("Correct ")
    score += 1
else:
    print("Incorrect ! ")
    print("Incorrect ! ")

print(f"you get {score} question correct")
print(f"you got {(score)/4*100}% ")
print("Welcome to DMK Quiz Game !")

playing = input("Do you want to play this game ? ")
if playing.lower() != "yes" :
    quit()
print("okay ! let's play <3")
score = 0

answer = input("What does AFK stand for ? ")
if answer.lower() == "away from keyboard" :
    print("Correct !")
    score +=1
else :
    print("Sorry Incorrect !")

answer = input("What is the capital of Tunisia ? ")
if answer.lower() == "tunis" :
    print("Correct !")
    score +=1
else :
    print("Sorry Incorrect :(")

answer = input("What does DMK stand for ? ")
if answer.lower() == "dammak" :
    print("Correct !")
    score +=1
else :
    print("Sorry Incorrect :(")

answer = input("What does nt stand for ? ")
if answer.lower() == "nice try" :
    print("Correct !")
    score +=1
else :
    print("Sorry Incorrect :(")

print("That's the END of the game i hope you enjoyed <3 ")
print("Your got "+str(score)+" questions correct !")
print("Your got "+str((score/4) *100)+"%. ")
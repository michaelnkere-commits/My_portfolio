print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Alright! Let's play :) ")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect.")
    
answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect.")
    
answer = input("What does HTTP stand for? ")

if answer.lower() == "hypertext transfer protocol":
    print("correct!")
    score += 1
else:
    print("Incorrect.")
    
answer = input("What does VGA stand for? ")

if answer.lower() == "video graphics array":
    print("correct!")
    
else:
    print("Incorrect.")

print(f"You're total score is {score}")
    
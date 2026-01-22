print("Welcome to the Adventure game")
name = input("What is your name? ")
print("Hello", name)

print("You are at crossroads.")
choice = input("Do you go left or rigth? ").lower()

if choice == "left":
    print("You enter the forest.")
    action = input("Do you climb a tree or keep walking? ").lower()

    if action == "climb":
        print("You spot a village from the top of the tree. You win!")
    elif action == "walk":
        print("You get lost in the forest. Game over ")
    else:
        print("Invalid choice. Game over")

elif choice == "right":
    print("You reach a river")
    action = input("Do you swim or turn back? ").lower()

    if action == "swim":
        print("You safely cross the river. You win")
    elif action == "back":
        print("You trip and fall. Game over.")
    else:
        print("Invalid choice. Game over")

else:
    print("That is not a valid choice")


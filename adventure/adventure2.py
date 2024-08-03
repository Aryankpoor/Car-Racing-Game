import keyboard

# Introduction
name = input("Type your name: ")
print("Hi", name, "Welcome to football master!\n")
print("In this game, you will play the career of a professional footballer\n")
print("Are you sure you are ready to go down this career path?\n")
start = input("Start Career?(y/n) ")

if start == "y" or start == "Y" :
    print("Brave Choice, not many are ready to take such a big responsibility.\n")
    print("Welcome to chapter 1: THE START IS BORN")
    print("In this game, you will encounter a lot of commands, all required to be run in a specific order and accuracy.")
    print("To start type '/commands' below to view all the commands for this game. Remember, wrong command and the game closes!!\n")
    init = input("")

    if init == '/COMMANDS' or init == '/commands':
        print("Your commands for chapter 1:\n")
        print()


elif start == "n" or start == "N":
    print("Don't want to play? Fine, your loss")
    print("Goodybe for now, something tells me we are gonna meet again...")
    exit()
else:
    print("Wrong key entered, maybe you do not have what it takes.")
    print("Goodbye")
    exit()
    
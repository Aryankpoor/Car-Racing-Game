name = input("Type your name: ")
print("Welcome", name, "to the new version of adventure!")

answer = input(
    "You are on a , it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    way = input("You come towards a dead end, but there is a hidden path to the left. Do you want to take it? (yes/no) ")

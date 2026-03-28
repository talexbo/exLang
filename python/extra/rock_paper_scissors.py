import random

computer = random.randint(1, 3)

print("===================")
print("Rock Paper Scissors")
print("===================")

print("1) ✊")
print("2) ✋")
print("3) ✌️ ")

icons = {
    1: "✊",
    2: "✋",
    3: "✌️"
}

player = int(input("Pick a number: "))
print(f"You chose {icons[player]}")
print(f"CPU chose {icons[computer]}")

if (player == computer):
    print("This ended in a draw. Recast.")
else:
    if (player == 1):
        if (computer == 2):
            print("The CPU won.")
        if (computer == 3):
            print("The player won.")
    if (player == 2):
        if (computer == 1):
            print("The player won.")
        if (computer == 3):
            print("The CPU won.")
    if (player == 3):
        if (computer == 1):
            print("The CPU won.")
        if (computer == 2):
            print("The player won.")

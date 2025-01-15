import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("type rock/ paper/scissors or q to press game")
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number].lower()
    print(f"computer chose {computer_pick}")

    if (user_input == "rock" and computer_pick == "scissors") or (user_input == "scissors" and computer_pick == "paper") or (user_input == "paper" and computer_pick == "rock"):
        print("you won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("it's a tie!")
    else:
        print("you lost!")
        computer_wins += 1

print("you won", user_wins, "times")
print("the computer won", computer_wins, "times.")
print("goodbye")
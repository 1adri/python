import random 
# Import random to select a choice from rock paper scissors in list
def answer_select():
    global answer
    answer = input("Select your choice: ")
    answer = answer.lower()
    if answer != "rock" and answer != "paper" and answer != "scissor":
        print("\nInvalid, Please Re-enter Your Choice!")
        return 
    
answer_select()

computer_choice_list = ["Rock", "Paper", "Scissor"]

computer_choice = random.choice(computer_choice_list)


if answer == "rock":
    if computer_choice == "Scissor":
        print("\nThe computer chose", computer_choice + ", you win!")
    else:
        print("\nThe computer chose", computer_choice + ", you lost.")
if answer == "paper":
    if computer_choice == "Rock":
        print("\nThe computer chose", computer_choice + ", you win!")
    else:
        print("\nThe computer chose", computer_choice + ", you lost.")
if answer == "scissor":
    if computer_choice == "Paper":
        print("\nThe computer chose", computer_choice + ", you win!")
    else:
        print("\nThe computer chose", computer_choice + ", you lost.")

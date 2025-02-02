import random

array = ["rock","paper","scissor"]

while Tr
    Computer_choice = random.choice(array)
    
    print(Computer_choice)
    
    user = input("Rock, Paper, Scissor: ").lower()
    
    if user == "cls" or user == "quit":
        break
    
    elif user == "rock" and Computer_choice == "rock" or user == "paper" and Computer_choice == "paper" or user == "scissor" and Computer_choice == "scissor":
        print("you are in draw")
    
    elif user == "rock" and Computer_choice == "scissor" or user == "paper" and Computer_choice == "rock" or user == "scissor" and Computer_choice == "paper":
        print("you won 🤩🤩")
    
    elif user == "rock" and Computer_choice == "paper" or user == "paper" and Computer_choice == "scissor" or user == "scissor" and Computer_choice == "rock":
        print("computer won 🤖🤖")
    
    else:
        print("invalid syntax")

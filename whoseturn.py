import time
import random
import os
from colorama import Fore, Back, Style
from getpass import getpass



#Whose turn is it anyways? Program for the kids to decide whose turn it is to choose.

class Child:
    def __init__(self, name, game_choice=False):
        self.name = name 
        self.game_choice = game_choice

def intro():
    print(""" 
    
    
    
 ____      ____  __                            _________                                            
|_  _|    |_  _|[  |                          |  _   _  |                                           
  \ \  /\  / /   | |--.   .--.   .--.  .---.  |_/ | | \_|__   _   _ .--.  _ .--.                    
   \ \/  \/ /    | .-. |/ .'`\ \( (`\]/ /__\\     | |   [  | | | [ `/'`\][ `.-. |                   
    \  /\  /     | | | || \__. | `'.'.| \__.,    _| |_   | \_/ |, | |     | | | |                   
     \/  \/     [___]|__]'.__.' [\__) )'.__.'   |_____|  '.__.'_/[___]   [___||__]                  
    _            _   _          _                                                           _____   
   (_)          (_) / |_       / \                                                         / ___ `. 
   __   .--.    __ `| |-'     / _ \     _ .--.    _   __  _   _   __  ,--.    _   __  .--.|_/___) | 
  [  | ( (`\]  [  | | |      / ___ \   [ `.-. |  [ \ [  ][ \ [ \ [  ]`'_\ :  [ \ [  ]( (`\] /  __.' 
   | |  `'.'.   | | | |,   _/ /   \ \_  | | | |   \ '/ /  \ \/\ \/ / // | |,  \ '/ /  `'.'. |_|     
  [___][\__) ) [___]\__/  |____| |____|[___||__][\_:  /    \__/\__/  \'-;__/[\_:  /  [\__) )(_)     
                                                 \__.'                       \__.'                   """) 

    input("Press 'Enter' to begin.")

#RNG decides who gets to pick the game

def pick_game():
    list_of_choices = [nolan, micah]
    choice = random.choice([nolan, micah])
    if choice == nolan:
        print("The Great Daddy's PC has chosen.....")
        time.sleep(2)
        print("Nolan!")
        nolan.game_choice = True
    if choice == micah:
        print("The Great Daddy's PC has chosen.....")
        time.sleep(2)
        print("Micah!")
        micah.game_choice = True 

def games():
    print("Here is the list of games: 'Rock Paper Scissors', 'Flip the Coin', and 'Closest to the Number'.")
    time.sleep(1)
    game_list = ['r', 'f', 'c']
    if nolan.game_choice == True:
        choice = input(f"Which game would you like to pick {nolan.name}?\nPress 'r' for 'Rock Paper Scissors'\nPress 'f' for 'Flip the Coin'\nPress 'c' for 'Closest to the Number'  ").lower()
        while choice not in game_list:
            choice = input(f"Sorry, that's not an option.\nPress 'r' for 'Rock Paper Scissors'\nPress 'f' for 'Flip the Coin'\nPress 'c' for 'Closest to the Number'  ").lower()
        time.sleep(2) 
        if choice == 'r':
            rps()
        elif choice == 'f':
            flip()
        elif choice == 'c':
            close_to_num()
    elif micah.game_choice == True:
        choice = input(f"Which game would you like to pick {micah.name}?\nPress 'r' for 'Rock Paper Scissors'\nPress 'f' for 'Flip the Coin'\nPress 'c' for 'Closest to the Number'  ").lower()
        while choice not in game_list:
            choice = input(f"Sorry, that's not an option.\nPress 'r' for 'Rock Paper Scissors'\nPress 'f' for 'Flip the Coin'\nPress 'c' for 'Closest to the Number'  ").lower()
        if choice == 'r':
            rps()
        elif choice == 'f':
            flip()
        elif choice == 'c':
            close_to_num()

#Rock Paper Scissor logic, basically a large series of if checks
def rps():
    choices = ['r', 'p', 's']
    print(f"You have picked 'Rock Paper Scissors'.")
    if nolan.game_choice == True:
        nolan_choice = getpass(f"{nolan.name} gets to pick first.\nDon't let {micah.name} see!\nPress 'r' for rock\nPress 'p' for paper\nPress 's' for scissors").lower()
        while nolan_choice not in choices:
            nolan_choice = getpass(f"Sorry, that's not an option.\nPress 'r' for rock\nPress 'p' for paper\nPress 's' for scissors").lower()
        time.sleep(2)
        micah_choice = getpass(f"Now it's {micah.name}'s turn to pick.\nPress 'r' for rock\nPress 'p' for paper\nPress 's' for scissors").lower()
        while micah_choice not in choices:
            micah_choice = getpass(f" Sorry, that's not an option.\nPress 'r' for rock\nPress 'p' for paper\nPress 's' for scissors").lower()
        os.system('clear||cls')
        print("Ok, the choices are in! Calculating...")
        time.sleep(2)
        if nolan_choice == micah_choice:
            print("You guys picked the same thing. We'll have to try again.")
            rps()   
        if nolan_choice == 'r' and micah_choice == 'p':
            print(f"{nolan.name}'s choice was 'Rock'. {micah.name}'s choice was 'Paper'.\nPaper trumps Rock.\n{micah.name} wins!")
            time.sleep(2)
            print(f"{micah.name} gets to choose.\nThanks for playing!")
        elif nolan_choice == 'r' and micah_choice == 's':
            print(f"{nolan.name}'s choice was 'Rock'. {micah.name}'s choice was 'Scissors'.\nRock smashes Scissors.\n{nolan.name} wins!")
            time.sleep(2)
            print(f"{nolan.name} gets to choose.\nThanks for playing!")
        elif nolan_choice == 'p' and micah_choice == 'r':
            print(f"{nolan.name}'s choice was 'Paper'. {micah.name}'s choice was 'Rock'.\nPaper trumps Rock.\n{nolan.name} wins!")
            time.sleep(2)
            print(f"{nolan.name} gets to choose.\nThanks for playing!")
        elif nolan_choice == 's' and micah_choice == 'r':
            print(f"{nolan.name}'s choice was 'Scissors'. {micah.name}'s choice was 'Rock'.\nRock smashes Scissors.\n{micah.name} wins!")
            time.sleep(2)
            print(f"{micah.name} gets to choose.\nThanks for playing!")
        elif nolan_choice == 'p' and micah_choice == 's':
            print(f"{nolan.name}'s choice was 'Paper'. {micah.name}'s choice was 'Scissors'.\nScissors cut Paper.\n{micah.name} wins!")
            time.sleep(2)
            print(f"{micah.name} gets to choose.\nThanks for playing!")
        elif nolan_choice == 's' and micah_choice == 'p':
            print(f"{nolan.name}'s choice was 'Scissors'. {micah.name}'s choice was 'Paper'.\nScissors cut Paper.\n{nolan.name} wins!")
            time.sleep(2)
            print(f"{nolan.name} gets to choose.\nThanks for playing!")
    if micah.game_choice == True:
        micah_choice = getpass(f"{micah.name} gets to pick first.\nDon't let {nolan.name} see!\nPress 'r' for rock\nPress 'p' for paper\nPress 's' for scissors").lower()
        while micah_choice not in choices:
            micah_choice = getpass(f"Sorry, that's not an option.\nPress 'r' for rock\nPress 'p' for paper\nPress 's' for scissors").lower()
        time.sleep(2)
        nolan_choice = getpass(f"Now it's {nolan.name}'s turn to pick.\nPress 'r' for rock\nPress 'p' for paper\nPress 's' for scissors").lower()
        while nolan_choice not in choices:
            nolan_choice = getpass(f" Sorry, that's not an option.\nPress 'r' for rock\nPress 'p' for paper\nPress 's' for scissors").lower()
        os.system('clear||cls')
        print("Ok, the choices are in! Calculating...")
        time.sleep(2)
        if nolan_choice == micah_choice:
            print("You guys picked the same thing. We'll have to try again.")
            rps()   
        if micah_choice == 'r' and nolan_choice == 'p':
            print(f"{micah.name}'s choice was 'Rock'. {nolan.name}'s choice was 'Paper'.\nPaper trumps Rock.\n{nolan.name} wins!")
            time.sleep(2)
            print(f"{nolan.name} gets to choose.\nThanks for playing!")
        elif micah_choice == 'r' and nolan_choice == 's':
            print(f"{micah.name}'s choice was 'Rock'. {nolan.name}'s choice was 'Scissors'.\nRock smashes Scissors.\n{micah.name} wins!")
            time.sleep(2)
            print(f"{micah.name} gets to choose.\nThanks for playing!")
        elif micah_choice == 'p' and nolan_choice == 'r':
            print(f"{micah.name}'s choice was 'Paper'. {nolan.name}'s choice was 'Rock'.\nPaper trumps Rock.\n{micah.name} wins!")
            time.sleep(2)
            print(f"{micah.name} gets to choose.\nThanks for playing!")
        elif micah_choice == 's' and nolan_choice == 'r':
            print(f"{micah.name}'s choice was 'Scissors'. {nolan.name}'s choice was 'Rock'.\nRock smashes Scissors.\n{nolan.name} wins!")
            time.sleep(2)
            print(f"{nolan.name} gets to choose.\nThanks for playing!")
        elif micah_choice == 'p' and nolan_choice == 's':
            print(f"{micah.name}'s choice was 'Paper'. {nolan.name}'s choice was 'Scissors'.\nScissors cut Paper.\n{nolan.name} wins!")
            time.sleep(2)
            print(f"{nolan.name} gets to choose.\nThanks for playing!")
        elif micah_choice == 's' and nolan_choice == 'p':
            print(f"{micah.name}'s choice was 'Scissors'. {nolan.name}'s choice was 'Paper'.\nScissors cut Paper.\n{micah.name} wins!")
            time.sleep(2)
            print(f"{micah.name} gets to choose.\nThanks for playing!")
#Coin flip logic, another set of if checks
def flip():
    choices = ['h', 't']
    pc_choice = random.choice(choices) 
    print("You have picked 'Flip the Coin'.")
    if nolan.game_choice == True:
        nolan_choice = input(f"{nolan.name} gets to pick first.\nPress 'h' for Heads\nPress 't' for Tails  ").lower()
        while nolan_choice not in choices:
            nolan_choice = input("Sorry, that's not an option.\nPress 'h' for Heads\nPress 't' for Tails  ").lower()
        time.sleep(1) 
        if nolan_choice == 'h':
            print(f"{nolan.name} has picked 'Heads'.")
            time.sleep(2)
            print(f"That means {micah.name} is 'Tails'.")
            time.sleep(1)
            print("Flipping the coin now...Ping!!!")
            time.sleep(2)
            if nolan_choice == pc_choice:
                print(f"The coin landed on 'Heads'! {nolan.name} wins the toss.")
                time.sleep(2)
                print(f"{nolan.name} gets to choose.")
                time.sleep(1)
                print("Thank you for playing!")
            elif nolan_choice != pc_choice:
                print(f"The coin landed on 'Tails'! {micah.name} wins the toss.")
                time.sleep(2)
                print(f"{micah.name} gets to choose.")
                time.sleep(1)
                print("Thank you for playing!")
        elif nolan_choice == 't':
            print(f"{nolan.name} has picked 'Tails'.")
            time.sleep(2)
            print(f"That means {micah.name} is 'Heads'.")
            time.sleep(1)
            print("Flipping the coin now...Ping!!!")
            time.sleep(2)
            if nolan_choice == pc_choice:
                print(f"The coin landed on 'Tails'! {nolan.name} wins the toss.")
                time.sleep(2)
                print(f"{nolan.name} gets to choose.")
                time.sleep(1)
                print("Thank you for playing!")
            elif nolan_choice != pc_choice:
                print(f"The coin landed on 'Heads'! {micah.name} wins the toss.")
                time.sleep(2)
                print(f"{micah.name} gets to choose.")
                time.sleep(1)
                print("Thank you for playing!")
    if micah.game_choice == True:
        micah_choice = input(f"{micah.name} gets to pick first.\nPress 'h' for Heads\nPress 't' for Tails  ").lower()
        while micah_choice not in choices:
            micah_choice = input("Sorry, that's not an option.\nPress 'h' for Heads\nPress 't' for Tails  ").lower()
        time.sleep(1) 
        if micah_choice == 'h':
            print(f"{micah.name} has picked 'Heads'.")
            time.sleep(2)
            print(f"That means {nolan.name} is 'Tails'.")
            time.sleep(1)
            print("Flipping the coin now...Ping!!!")
            time.sleep(2)
            if micah_choice == pc_choice:
                print(f"The coin landed on 'Heads'! {micah.name} wins the toss.")
                time.sleep(2)
                print(f"{micah.name} gets to choose.")
                time.sleep(1)
                print("Thank you for playing!")
            elif micah_choice != pc_choice:
                print(f"The coin landed on 'Tails'! {nolan.name} wins the toss.")
                time.sleep(2)
                print(f"{nolan.name} gets to choose.")
                time.sleep(1)
                print("Thank you for playing!")
        elif micah_choice == 't':
            print(f"{micah.name} has picked 'Tails'.")
            time.sleep(2)
            print(f"That means {nolan.name} is 'Heads'.")
            time.sleep(1)
            print("Flipping the coin now...Ping!!!")
            time.sleep(2)
            if micah_choice == pc_choice:
                print(f"The coin landed on 'Tails'! {micah.name} wins the toss.")
                time.sleep(2)
                print(f"{micah.name} gets to choose.")
                time.sleep(1)
                print("Thank you for playing!")
            elif micah_choice != pc_choice:
                print(f"The coin landed on 'Heads'! {nolan.name} wins the toss.")
                time.sleep(2)
                print(f"{nolan.name} gets to choose.")
                time.sleep(1)
                print("Thank you for playing!")
#Closest to number logic. A Number between 1 and 50 is randomly generated, then each kid picks a number in that range.
#The random number is subtracted from each kid's number and the absolute value is taken. Whichever is the smallest wins.
def close_to_num():
    choices = []
    for num in range(1,51):
        choices.append(num)
    pc_choice = random.choice(choices) 
    print("You have picked 'Closest to the Number'.")
    time.sleep(1)
    if nolan.game_choice == True:
        nolan_choice = int(input(f"{nolan.name} gets to pick first.\nPick and type a number between 1 and 50.  "))
        while nolan_choice not in choices:
            nolan_choice = int(input("Sorry, that's not a valid option.\nPick and type a number between 1 and 50.  "))
            time.sleep(1)
        micah_choice = int(input(f"Now it's {micah.name}'s turn.\nPick and type a number between 1 and 50.  "))
        while micah_choice not in choices:
            micah_choice = int(input("Sorry, that's not a valid option.\nPick and type a number between 1 and 50.  "))
        print("Let's see who is closest. Calculating...")
        time.sleep(2)
        print(f"{nolan.name}'s choice was {nolan_choice}. {micah.name}'s choice was {micah_choice}.")
        time.sleep(1)
        print(f"The Great Daddy's PC's choice was...{pc_choice}.")
        if abs(nolan_choice - pc_choice) < abs(micah_choice - pc_choice):
            print(f"\n{nolan.name}'s choice was closest to the number. {nolan.name} wins!")
            time.sleep(2)
            print(f"{nolan.name} gets to choose.")
            time.sleep(1)
            print("\nThank you for playing!")
        elif abs(nolan_choice - pc_choice) > abs(micah_choice - pc_choice):
            print(f"\n{micah.name}'s choice was closest to the number. {micah.name} wins!")
            time.sleep(2)
            print(f"{micah.name} gets to choose.")
            time.sleep(1)
            print("\nThank you for playing!")
        elif abs(nolan_choice - pc_choice) == abs(micah_choice - pc_choice):
            print("It's a tie! We have to try again.")
            time.sleep(2)
            close_to_num()
    if micah.game_choice == True:
        micah_choice = int(input(f"{micah.name} gets to pick first.\nPick and type a number between 1 and 50.  "))
        while micah_choice not in choices:
            micah_choice = int(input("Sorry, that's not a valid option.\nPick and type a number between 1 and 50.  "))
            time.sleep(1)
        nolan_choice = int(input(f"Now it's {nolan.name}'s turn.\nPick and type a number between 1 and 50.  "))
        while nolan_choice not in choices:
            nolan_choice = int(input("Sorry, that's not a valid option.\nPick and type a number between 1 and 50.  "))
        print("Let's see who is closest. Calculating...")
        time.sleep(2)
        print(f"{micah.name}'s choice was {micah_choice}. {nolan.name}'s choice was {nolan_choice}.")
        time.sleep(1)
        print(f"The Great Daddy's PC's choice was...{pc_choice}.")
        if abs(micah_choice - pc_choice) < abs(nolan_choice - pc_choice):
            print(f"\n{micah.name}'s choice was closest to the number. {micah.name} wins!")
            time.sleep(2)
            print(f"{micah.name} gets to choose.")
            time.sleep(1)
            print("\nThank you for playing!")
        elif abs(micah_choice - pc_choice) > abs(nolan_choice - pc_choice):
            print(f"\n{nolan.name}'s choice was closest to the number. {nolan.name} wins!")
            time.sleep(2)
            print(f"{nolan.name} gets to choose.")
            time.sleep(1)
            print("\nThank you for playing!")
        elif abs(micah_choice - pc_choice) == abs(nolan_choice - pc_choice):
            print("It's a tie! We have to try again.")
            time.sleep(2)
            close_to_num()

intro()
os.system('clear||cls')
print(f"Who will pick the game? Let \"The Great Daddy's PC\" Decide.")
time.sleep(2) 
print_list = ["Randomizing randomizer...", "Reticulating Splines...", "Building Databases...", "Hold Please..."]
print(random.choice(print_list))
time.sleep(3)

#Creating instances

nolan = Child("Nolan")
micah = Child("Micah")

pick_game()
games()






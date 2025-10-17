#Module with functions for virtual critter program

import random
import games

def welcome():
    print("Welcome to the virtual critter program!")
    print("Here you can take care of your pets")
    print("Keep good care of them by feeding them playing with them and more!")


def create_critter(c1):
    print("What name do you want to give your critter?")
    name = input("▷ ")
    name = name.capitalize()
    c1.name_critter(name)

def random_personality():
    personalities = ["Calm", "Lazy", "Energetic"]
    choice = random.choice(personalities)
    return choice

def hunger(hunger):
    show = ""
    show += hunger*"■"
    show += (10-hunger)*"□"
    return show

def selection(ref):
        print("What do you want to do?")
        print("""
        1 - INFO
        2 - CHECK
        3 - FEED
        4 - PLAY
        5 - MORE
        6 - EXIT PROGRAM
              """)
        x = int(input("▷ "))
        if(x==1):
            ref.info_c()
        elif(x==2):
            ref.mood()
            print("Hunger:",hunger(ref.hunger))
        elif(x==3):
            ref.feed()
        elif(x==4):
            play(ref, ref.name)
        elif(x==6):
            print("See you later!")
            return False
        return True

def play(ref, name):
    print("""
What game do you want to play?
    1 - HANGMAN
    2 - TICTACTOE
    3 - BACK
    """)
    x = int(input("▷ "))
    if(x==1):
        games.hangman(name)
    elif(x==2):
        games.tictactoe(name)
    elif(x==3):
        return
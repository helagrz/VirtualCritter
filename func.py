#Module with functions for virtual critter program

import random

def welcome():
    print("Welcome to the virtual critter program!")
    print("Here you can take care of your pets")
    print("Keep good care of them by feeding them playing with them and more!")


def create_critter(c1):
    print("What name do you want to give your critter?")
    name = input()
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
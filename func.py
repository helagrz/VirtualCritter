#Module with functions for virtual critter program

import random

def create_critter(c1):
    print("What name do you want to give your critter?")
    name = input()
    name = name.capitalize()
    c1.name_critter(name)

def random_personality():
    personalities = ["Calm", "Lazy", "Energetic"]
    choice = random.choice(personalities)
    return choice
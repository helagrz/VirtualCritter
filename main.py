import random

def random_personality():
    personalities = ["Calm", "Lazy", "Energetic"]
    choice = random.choice(personalities)
    return choice

def create_critter(c1):
    print("What name do you want to give your critter?")
    name = input()
    name = name.capitalize()
    c1.name_critter(name)


class critter(object):
    """A virtual pet"""
    total = 0

    @staticmethod
    def status():
        print("You have",critter.total,"critters!")

    
    def __init__(self):
        print("A new critter has been born!")
        self.name = ""
        self.pers = random_personality()
        critter.total+=1

    def __str__(self):
        info = "Critter info:\n"
        info += "   Name: " + self.name + "\n"
        info += "   Personality: " + self.pers + "\n"
        return info

    def name_critter(self, name):
        self.name = name

c1 = critter()
create_critter(c1)

print(critter.total)

c2 = critter()
create_critter(c2)

print(critter.total)

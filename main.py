class critter(object):
    """A virtual pet"""
    def __init__(self):
        print("A new critter has been born")
        self.name = ""

    def __str__(self):
        info = "Critter info:\n"
        info += "   Name: " + self.name + "\n"
        return info

    def name_critter(self, name):
        self.name = name

c1 = critter()
print("What name do you want to give your critter?")
name = input()
name = name.capitalize()
c1.name_critter(name)
print(c1)

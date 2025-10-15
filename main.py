import func

class critter(object):
    """A virtual pet"""
    total = 0

    @staticmethod
    def status():
        print("You have",critter.total,"critters!")

    
    def __init__(self):
        print("A new critter has been born!")
        self.name = ""
        self.pers = func.random_personality()
        critter.total+=1
        self.__mood = "neutral"

    def __str__(self):
        info = "Critter info:\n"
        info += "   Name: " + self.name + "\n"
        info += "   Personality: " + self.pers + "\n"
        return info

    def name_critter(self, name):
        self.name = name

    def mood(self):
        print("Right now I feel",self.__mood)

c1 = critter()
func.create_critter(c1)

print(c1)


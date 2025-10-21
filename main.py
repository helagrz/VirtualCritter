import func
import games

class critter(object):
    """A virtual pet"""
    total = 0
    current = 0

    @staticmethod
    def status():
        print("You have",critter.total,"critters!")

    
    def __init__(self):
        print("A new critter has been born!")
        self.name = ""
        self.pers = func.random_personality()
        critter.total+=1
        self.__mood = "neutral"
        self.hunger = 5

    def __str__(self):
        info = "Critter info:\n"
        info += "   Name: " + self.name + "\n"
        info += "   Personality: " + self.pers + "\n"
        return info
        
    def info_c(self):
        info = "Critter info:\n"
        info += "   Name: " + self.name + "\n"
        info += "   Personality: " + self.pers + "\n"
        print(info)

    def name_critter(self, name):
        self.name = name

    def mood(self):
        print(self.name,"feels",self.__mood)

    def feed(self):
        if(self.hunger >= 10):
            print(self.name,"is full")
            print(func.hunger(self.hunger))
            self.hunger = 10
        else:
            self.hunger += 2
            print("You gave",self.name,"food")
            print("Level of hunger:")
            print(func.hunger(self.hunger))

#c1 = critter()
#func.create_critter(c1)
continue_pl = True
#print(c1)

c = []
c.append(critter())
func.create_critter(c[0])

while(continue_pl):
    continue_pl = func.selection(c[critter.current], c, critter)
    print(critter.current)
    
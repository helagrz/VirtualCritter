import func
import games

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
        self.hunger = 5

    def __str__(self):
        return self.info_c()
        
    def info_c(self):
        info = "Critter info:\n"
        info += "   Name: " + self.name + "\n"
        info += "   Personality: " + self.pers + "\n"
        print(info)
        return info

    def selection(self):
        print("What do you want to do?")
        print("""
            1 - INFO
            2 - CHECK
            3 - FEED
            4 - PLAY
            5 - MORE
              """)
        x = int(input())
        match x:
            case 1:
                print("You selected: INFO")
                self.info_c()


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

c1 = critter()
func.create_critter(c1)

continue_pl = True
print(c1)

c1.selection()


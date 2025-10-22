import func
import datetime

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
        self.mood = 3
        self.hunger = 5
        self.level = 10

    def __str__(self):
        info = "Critter info:\n"
        info += "   Name: " + self.name + "\n"
        info += "   Personality: " + self.pers + "\n"
        info += "   Level : " + str(self.level//10) + "\n"
        return info
        
    def info_c(self):
        info = "Critter info:\n"
        info += "   Name: " + self.name + "\n"
        info += "   Personality: " + self.pers + "\n"
        info += "   Level : " + str(self.level//10) + "\n"
        print(info)

    def name_critter(self, name):
        self.name = name

    def mood_str(self):
        x = ""
        match self.mood:
            case 1:
                x ='very bad'
            case 2:
                x ='bad'
            case 3:
                x ='neutral'
            case 4:
                x ='happy'
            case 5:
                x ='awesome'
        return x

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
    
continue_pl = True
c = []
minutes = int(datetime.datetime.now().strftime("%M"))

#print('Do you have a save file you want to load? (to proceed enter \'yes\')')
#x = input("▷ ")
#if(x == 'yes'):
func.load(c, critter, 'autosave.txt')
#else:
#    c.append(critter())
#    func.create_critter(c[0])

while(continue_pl):
    continue_pl = func.selection(c[critter.current], c, critter)
    print(critter.current)
    func.save(c, critter, 'autosave.txt')
    #print(func.level(c[critter.current].level))

    
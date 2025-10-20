#Module with functions for virtual critter program

import random
import games
import os

SaveFile = open('./savefile.txt', 'r')

def load_file(c, f, index):
    c[index].name_critter(f.readline())
    c[index].pers = f.readline()
    c[index].hunger = int(f.readline())

def load(c, o_ref):
    cwd = os.getcwd()
    cwd = os.path.join(cwd,'VirtualCritter')
    c.clear()
    c.append(o_ref)
    o_ref.total = 0
    cwd_s = os.path.join(cwd,'savefile.txt')
    with open(cwd_s, 'r') as f:
        t = int(f.readline())
        for i in range(t):
            c.append(o_ref)
            load_file(c, f, i)
    f.close()


def welcome():
    print("Welcome to the virtual critter program!")
    print("Here you can take care of your pets")
    print("Keep good care of them by feeding them playing with them and more!")


def create_critter(c):
    print("What name do you want to give your critter?")
    name = input("▷ ")
    name = name.capitalize()
    c.name_critter(name)

def random_personality():
    personalities = ["Calm", "Lazy", "Energetic"]
    choice = random.choice(personalities)
    return choice

def hunger(hunger):
    show = ""
    show += hunger*"■"
    show += (10-hunger)*"□"
    return show

def valid_name(s):
    return True

def critter_selection(ref, c, o_ref):
    print(ref.status())
    j = 1
    symbol = ""
    for i in c:
        if((ref.current+1)==j):
            symbol = '▶ '
        else:
            symbol = str(j)
            symbol += " - "
        print("            "+symbol+i.name.upper())
        j+=1
    x = int(input("▷ "))
    for i in range(len(c)):
        if(i == x and x!=ref.current+1):
            print("You choose",c[i-1].name)
            o_ref.current = x-1



def selection(ref, c, o_ref):
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
        elif(x==5):
            settings(ref, c, o_ref)
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
    
def settings(ref, c, o_ref):
    print("""
What do you want to do?
    1 - CHANGE NAME
        

    3 - SAVE CRITTER
    4 - LOAD CRITTER
    5 - CREATE NEW CRITTER
    6 - REMOVE THIS CRITTER
    7 - BACK
""")
    x = int(input("▷ "))
    if(x==1):
        print("What new name do you want to give",ref.name)
        x = input("▷ ")
        while(not(valid_name(x))):
            print("Name not valid")
            print("Name has to include at least one letter")
            x = input("▷ ")
        x = x.capitalize()
        print(ref.name,"is now", x)
        ref.name_critter(x)
    elif(x==4):
        load(c, o_ref)
    elif(x==5):
        print("Are you sure you want to add another critter? (To proceed enter \'yes\')")
        answer = input("▷ ")
        answer = answer.lower()
        if(answer=='yes'):
            c.append(o_ref())
            create_critter(c[o_ref.total-1])
            o_ref.current = o_ref.total-1
            print(c[o_ref.current])
    elif(x==6):
        print("Are you sure? (To proceed enter \'yes\')")
        answer = input("▷ ")
        answer = answer.lower()
        if(answer=='yes'):
            for i in c:
                print(i)
            c.pop(o_ref.current)
            o_ref.total -= 1
            o_ref.current = len(c)-1
    elif(x==7):
        critter_selection(ref, c, o_ref)
    return
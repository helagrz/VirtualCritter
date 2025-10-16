def tictactoe(name):
    def table(tab):
        print(tab[0],"|",tab[1],"|",tab[2])
        print("-"*9)
        print(tab[3],"|",tab[4],"|",tab[5])
        print("-"*9)
        print(tab[6],"|",tab[7],"|",tab[8])

    def check(tab):
        if(((tab[0]==tab[1] and tab[1]==tab[2]) and tab[0]!=" ") or ((tab[3]==tab[4] and tab[4]==tab[5])and tab[3]!=" ") or ((tab[6]==tab[7] and tab[7]==tab[8])and tab[6]!=" ")):
            return True
        elif((tab[0]==tab[3] and tab[3]==tab[6]and tab[3]!=" ") or (tab[1]==tab[4] and tab[4]==tab[7]and tab[4]!=" ") or (tab[2]==tab[5] and tab[5]==tab[8]and tab[2]!=" ")):
            return True
        elif((tab[0]==tab[4] and tab[4]==tab[8]and tab[4]!=" ")or (tab[2]==tab[4] and tab[4]==tab[6])and tab[2]!=" "):
            return True
        else:
            return False

    def get3(a,b,c):
        if((a!= " " and a==b and c==" ")or(b!= " " and b==c and a==" ")or(a!= " " and a==c and b==" ")):
            return True
        else:
             return False

    def computer(tab):
        pos = [0,1,2,3,4,5,6,7,8, 0,3,6,1,4,7,2,5,8 ,0,4,8,2,4,6]
        i = 0
        for j in range(8):
            if(get3(tab[pos[i]],tab[pos[i+1]],tab[pos[i+2]])):
                if(tab[pos[i]]==" "):
                    return pos[i]
                elif(tab[pos[i+1]]==" "):
                    return pos[i+1]
                else:
                    return pos[i+2]
            i+=3
        return -1

    import random
    print("TIC-TAC-TOE")
    print("""
    You will play with""",name,"""by turns
    To place a symbol write of of the numbers below:

    1 | 2 | 3 
    ---------
    4 | 5 | 6 
    ---------
    7 | 8 | 9      
    """)
    tab = [" "," "," "," "," "," "," "," "," "]
    print("Choose a symbol (O or X)")
    s = input()
    s = s.upper()
    while(s!='O' and s!='X'):
        print("Choose a symbol (O or X)")
        s = input()
        s = s.upper()

    if(s=="X"):
        cs = "O"
    else:
        cs="X"

    player_starts = bool(random.choice([True,False]))
    if(player_starts):
        print("You start!")
        table(tab)
    else:
        print(name,"starts!")
        x = random.randint(1,9)
        while(tab[x-1]!=" "):
            x = random.randint(1,9)
        tab[x-1]=cs
        table(tab)
        print("Your turn")

    win = False
    winner = ""
    space = True

    while(win == False and space == True):
        x = int(input())
        while(x>9 and x<1):
            print("Enter numbers 1-9")
            x = int(input())
        while(tab[x-1]!=" "):
            print("This space is taken")
            x = int(input())
        tab[x-1]=s
        table(tab)

        win = check(tab)
        space = " " in tab
        winner = s

        if(win==False and space==True):
            print(str(name)+"'s turn")
            if(computer(tab)==-1):
                x = random.randint(1,9)
                while(tab[x-1]!=" "):
                    x = random.randint(1,9)
                tab[x-1]=cs
            else:
                tab[computer(tab)]=cs
            table(tab)
            win = check(tab)
            winner = cs
            space = " " in tab
            if(space==True):
                print("Your turn")

    if(space==False and win==False) :
        print("No space left, nobody wins")
    else:
        print(winner,"wins!")
        if(winner ==s):
            print("Congratulations!")
        else:
            print("You lose,",name,"wins!")

    return
    
def hangman(name):
    hangman = ("""






    ____________
    """,
    """

    |    
    |      
    |     
    |        
    |
    |___________
    """
    ,
    """
    ____________
    |     
    |      
    |     
    |       
    |
    |___________
    """
    ,
    """
    ____________
    |  /     |
    | /      
    |/      
    |        
    |
    |___________
    """
    ,
    """
    ____________
    |  /     |
    | /      O
    |/      
    |        
    |
    |___________
    """
    ,
    """
    ____________
    |  /     |
    | /      O
    |/       |
    |        
    |
    |___________
    """
    ,
    """
    ____________
    |  /     |
    | /      O
    |/      /|
    |        
    |
    |___________
    """
    ,
    """
    ____________
    |  /     |
    | /      O
    |/      /|\ 
    |       
    |
    |___________
    """
    ,
    """
    ____________
    |  /     |
    | /      O
    |/      /|\ 
    |        /
    |
    |___________
    """
    ,
    """
    ____________
    |  /     |
    | /      O
    |/      /|\ 
    |        /\ 
    |
    |___________
    """
    )
    import random
    dif1 = ["PYTHON", "HANGMAN", "COMPUTER", "GAMES", "UNIVERSITY", "WORLD", "KEYBOARD", "PHONE"]
    dif2 = ["HELLO WORLD", "COMPUTER SCIENCE", "VIDEO GAMES", "NOTTINGHAM TRENT UNIVERSITY", "PYTHON HANGMAN GAME"]
    words_arr = []

    dif1.append(name.upper())

    print("HANGMAN GAME")
    print("Enter various letters to guess "+str(name)+"'s word or sentence")
    print("You can also enter whole words or phrases to make a guess")
    print("What difficulty? (Easy - singular world, or hard - sentences)")
    dif = input()
    dif = dif.lower()

    while(dif!="easy" and  dif!="hard"):
        print("Write 'easy' of 'hard'")
        dif = input()
        dif = dif.lower()

    if(dif=="easy"):
        words_arr = dif1
    else:
        words_arr = dif2

    word = random.choice(words_arr)
    wrong = []
    answer = ""
    hangman_index = 0

    answer += '_'*len(word)
    for i in range(len(word)):
                if(word[i]==" "):
                    pomlist = list(answer)
                    pomlist[i]=" "
                    answer = "".join(pomlist)
    print(answer)

    while(answer!=word and hangman_index<10):
        letter = input()
        letter = letter.upper()
        if(len(letter)>1):
            if(letter==word):
                print("You guesses it!")
                answer = word
            else:
                print("Wrong guess, it's not",letter)
        else:
            if((letter in word) and not(letter in answer)):
                for i in range(len(word)):
                    if(word[i]==letter):
                        pomlist = list(answer)
                        pomlist[i]=letter
                        answer = "".join(pomlist)
            elif((letter in answer) or (letter in wrong)):
                print("You already guessed that letter")
            else:
                wrong.append(letter)
                print(hangman[hangman_index])
                hangman_index+=1
                print("No",letter)
                print("Missing letters:",wrong)
        print(answer)

    if(hangman_index<10):
        print("\nCongratulations! You win!")
    else:
        print("\nYou lose")
        if(dif =="easy"):
            print("The word was",word)
        else:
            print("The sentence was",word)
    print("")

def re(a,p,q):
    y=p[:a]+q[a]+p[a+1:]
    return y
dd=1.1
flag=1
print
print'------------------------X---------------------------'
print
print
print'\tHANGMAN GAME (modified)\n\tWord guessing game.'
print
while True:
    while True:
        print
        print
        print
        print
        print' MENU  (modified mode)\n(press corresponding serial number to access)\n\n1. NEW GAME\n2. INSTRUCTIONS\n3. EXIT to Main Menu'
        print
        print"Let's Go!"
        print
        c=['desiccate','radian','degree','telegraph','statesman','hybridisation','torque','equilibrium','chromosome','hormone','library','calendar','breakfast','kolkata','hyperconjugation','argument','modulus','trigonometry','thermometer','resistance','contagious','technology','conjugation','resonance','frequency','haematology','meteorology','punctual','kingfisher','microsoft','newton','einstein','galileo','psychology','hypothalamus','continental','xerophyte','programmer','assessment','bibliography','renaissance','microbiology','engineering','refrigerator']
        while True:
            import random
            d=random.randint(0,len(c)-1)
            if d!=dd:
                break
        dd=d
        e=c[d]
        j=[]
        for f in range(len(e)/2+3):
            import random
            g=random.randint(0,len(e)-1)
            e=e.replace(e[g],'-')
            j.append(g)
        print

        a=raw_input("(Select key and press enter) ")
        print
        if a=='2':
            print
            print
            print'\tINSTRUCTIONS:-\n\n\t1. Hangman is a word guessing game.\n\t2. A secret word will be selected and the player tries to determine the word.\n\t3. Three chances will be given to determine the word.\n\t4. After each failure a hint would be given.\n\t5. Press ENTER to continue.\n\t6. For immediate exit from gameplay to MENU press HASH( # ) then ENTER.'
            print
            print"\tNow let's play!"
            print
            b=raw_input('<=BACK')
            
            print
            print'------------X-----------------'
            break
        elif a=='3':
            print
            print
            print '\t\tQuiting the game.'
            print
            print'\t\t\t\tThank You!'
            print
            print'--------------------------X-----------------------------'
            print
            print'\t\t< By Tamojit Das >'
            print
            print
            hj=raw_input('')
            flag=2
            break
        else:
            print
            print
            print'\tGuess the word.'
            print
            print
            k=0
            i=0
            while i<(3):
                print'\t',e
                print
                h=raw_input('===> ')
                h=h.lower()
                if h=='#':
                    break
                if h.lower()==c[d]:
                    print
                    print'\tExcellent!\n\tYou have won!\t\tCongratulations.'
                    print
                    print
                    break
                print
                if i<2:
                    print'Get a hint.'
                    print
                    print'Try again.'
                print
                e=re(j[k],e,c[d])
                i=i+1
                k=k+1
            else:
                print
                print'\t\tGame Over!\n\nYou have lost all of your chances.\n\nThe word was ',c[d],'.'
                print
            print
            print
            l=raw_input('<==BACK')
            
            print
            print
            print'-------------X---------------'
            break
    if flag==2:
        break

    
    
    
    


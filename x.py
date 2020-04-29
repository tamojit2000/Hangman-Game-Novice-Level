def qw(d,e,f):
    l=[]
    for a in range(len(f)):
        if d==f[a]:
            l.append(a)
    g=''
    for x in range(len(f)):
        if x not in l:
            g=g+e[x]
        else:
            g=g+f[x]
    return g
def score(a,b,c):
    if c==0:
        print'\tSCORE BOARD\n\n'
        print'\tYour score is ',st
    elif c==4:
        print'\tSCORE BOARD\n\n'
        print'\tYour score is ',b*5
    else:
        print'\tSCORE BOARD\n\n'
        print'\tYour score is ',a-b

        
dd=1.1
flag=0
print
print'------------------------X---------------------------'
print
print
print'\tHANGMAN GAME (original)\n\tWord guessing game.'
print
while True:
    while True:
        print
        print
        print
        print
        print' MENU  (original mode)\n(press corresponding serial number to access)\n\n1. NEW GAME\n2. INSTRUCTIONS\n3. EXIT to Main Menu'
        print
        print"Let's Go!"
        print
        c=['desiccate','radian','degree','telegraph','statesman','torque','hybridisation','equilibrium','chromosome','hormone','library','calendar','breakfast','kolkata','hyperconjugation','argument','modulus','trigonometry','thermometer','resistance','contagious','technology','conjugation','resonance','frequency','haematology','meteorology','punctual','kingfisher','microsoft','newton','einstein','galileo','psychology','hypothalamus','continental','xerophyte','programmer','assessment','bibliography','renaissance','microbiology','engineering','refrigerator']
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
            print'\tINSTRUCTIONS:-\n\n\t1. Hangman is a word guessing game.\n\t2. A secret word will be selected and the player tries to determine the word.\n\t3. Player enters a letter, if it is present in word the said letters are unlocked, also player may enter the whole word if confident.\n\t4. Four chances are given.\n\t5. Scoring system is arranged.\n\t6. Correct entry on first chance gives 100 points, correct entry after several chance decreases points, total failure leads to 0 points.\n\t7. Press ENTER to continue.\n\t8. For immediate exit from gameplay to MENU press HASH( # ) then ENTER.'
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
            print
            print'\t\t< By Tamojit Das >'
            print
            print
            hj=raw_input('')
            flag=9
            break
        else:
            st=0
            ab=0
            print
            print
            print'\tGuess the word.\n\n\tEnter guessed letter.\n\n'
            print
            print
            k=3
            i=0
            while i<(4):
                print'\t',e
                print
                h=raw_input('===> ')
                h=h.lower()
                if h=='#':
                    break
                if h==c[d]:
                    print
                    print'\tExcellent!\n\n\tYou have won!\t\tCongratulations.'
                    print
                    print
                    st=100
                    break
                if h!='':
                    if h in c[d]:
                        e=qw(h,e,c[d])
                        print'\t',e
                        print
                        print'\t\t',h,'is filled in the blank.'
                        ab=ab+2
                if h.lower() not in c[d]:
                    print '\t',h,'is absent in word.'
                print
                print
                if k>0:
                    print'\t\t\tChances left:',k
                if k==1:
                    print'\n\t\tNow guess the whole word.\n'
                i=i+1
                k=k-1
            else:
                print
                print'\t\tGame Over!\n\nYou have lost all of your chances.\n\nThe word was ',c[d],'.'
                print
            print
            score(st,ab,i)
            print
            print
            l=raw_input('<==BACK')
            
            print
            print
            print'-------------X---------------'
            break
    if flag==9:
        break

    
    
    
    


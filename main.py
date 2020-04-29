from random import randint,choice

def place(word,source,x):
    word=list(word)
    for a in range(len(source)):
        if source[a]==x:
            word[a]=x
    z=''
    for i in word:
        z+=i
    return z

def form_object(x):
    p=len(x)
    a=[i for i in range(1,p,randint(2,p-1))]
    z=''
    dash=set()
    for c in range(p):
        if c in a:
            z+='-'
            dash.add(x[c])
        else:
            z+=x[c]
    for a in dash:
        z=z.replace(a,'-')
    return (z,len(dash))
    
f=open('data.txt','r')
word_list=f.read().split()
f.close()


subject=choice(word_list)
obj=form_object(subject)
turns=obj[1]
score=0
increment=100.0/turns

obj=obj[0]

a=1
while a<turns+1:
    print '='*50
    print '\nTurn: ',a,'\tChances: ',turns,'\tScore: ',score
    print '\n',obj,'\n'
    b=raw_input('>>> ')
    if b in subject:
        print '\nOk, we place the letter.'
        obj=place(obj,subject,b)
        a+=1
        score+=increment
        if obj==subject:
            print '\nThe Word is ',subject
            break

    elif b in obj:
        print '\nLetter is already there.'

    else:
        print '\nOops the letter is not in the word.'
        a+=1
    print '='*50
else:
    print'\nYou have lost all your chances.\nThe word was ',subject
print '\nYour Score: ',score
raw_input('Thank you.')


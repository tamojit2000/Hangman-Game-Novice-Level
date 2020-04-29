from Tkinter import *
from random import *
import winsound

def remove_press_enter_label(event):
    press_enter_label.place_forget()
    play_frame.place(x=0,y=150)
    pre_play_game()
#    play_game()

def display_instruction():
    global rootA,rootB
    try:
        rootB.destroy()
    except:
        pass
    rootA=Tk()
    rootA.geometry('500x500+400+100')
    rootA.title('Instruction')
    w=Listbox(rootA,bg='lawn green',font=('Arial',18))
    s='''
    This is a game where you need to guess
    the missing letters in the word.
    Write the letters one by one
    and press next.
    Score and chances are arranged
    automatically.

    '''
    s=s.split('\n')
    for c in range(len(s)):
        w.insert(c+1,s[c])
    w.pack(expand=YES,fill=BOTH)


    rootA.mainloop()


def display_credits():
    global rootA,rootB
    try:
        rootA.destroy()
    except:
        pass
    rootB=Tk()
    rootB.geometry('500x500+400+100')
    rootB.title('Credits')
    w=Listbox(rootB,bg='lawn green',font=('Arial',18))
    s='''
    Tamojit Das

    Iem CSE
    1st Year
    '''
    s=s.split('\n')
    for c in range(len(s)):
        w.insert(c+1,s[c])
    w.pack(expand=YES,fill=BOTH)


    rootB.mainloop()


def Next():
    pass

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
    a=[i for i in range(1,p,2)]
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


def pre_play_game(event=None):
    global word_list,subject,obj,score,increment,turns,chances,start
    
    f=open('data.txt','r')
    word_list=f.read().split()
    f.close()

    subject=choice(word_list)
    obj=form_object(subject)
    chances=obj[1]
    score=0
    start=0
    increment=100.0/chances
    obj=obj[0]
    characteristics.config(text='Guess the letters.')    
    display.config(text=obj)
    score_label.config(text='Score: '+str(score))
    turns_label.config(text='Turn: '+str(start))
    chances_label.config(text='Chances: '+str(chances))

    Next.config(text='Next',command=play_game)
    root.bind('<Return>',play_game)
    
def play_game(event=None):
    global word_list,start,turns,score,subject,obj,increment
    
    #print start,chances  
    b=entry.get()
    if start<chances:
        
        #print b
        if b in subject:
            #if start!=1:
            characteristics.config(text='Ok, we place the letter.')
            obj=place(obj,subject,b)
            #print 'ok'
            start+=1
            score+=increment
            
            
                

        elif b in obj:
            characteristics.config(text='Letter is already there.')

        else:
            characteristics.config(text='Oops the letter is not in the word.',fg='red')
            start+=1
        turns_label.config(text='Turn: '+str(start))
    else:
        if subject!=obj:
            characteristics.config(text='You have lost all your chances.The word was '+subject)
            
        else:
            characteristics.config(text='You got the word.')

        Next.config(text='Retry',command=pre_play_game)
        root.bind('<Return>',pre_play_game)
        #print 'done'
    
    entry.delete(0,END)
    display.config(text=obj)
    score_label.config(text='Score: '+str(score))
    
    chances_label.config(text='Chances: '+str(chances))


winsound.PlaySound('background.wav',winsound.SND_NODEFAULT|winsound.SND_ASYNC|winsound.SND_LOOP)

rootA=None
rootB=None

root=Tk()
root.title('Hangman')
root.geometry('1600x900')
root.state('zoomed')
root.config(background='lawn green')
Frame(root,height=150,width=1600,background='forest green').place(x=0,y=0)
Label(root,text='Hangman Game',font=('Comic Sans MS',60,'bold'),bg='forest green',fg='red').place(x=20,y=33)

press_enter_label=Label(root,text='Press Enter to Start....',font=('Arial',32),bg='lawn green',fg='forest green')
press_enter_label.place(x=400,y=450)
root.bind('<Return>',remove_press_enter_label)

Button(root,text='Instruction',font=('Arial',16),bg='forest green',fg='red',command=display_instruction,width=10,activebackground='lawn green').place(x=1050,y=108)
Button(root,text='Credits',font=('Arial',16),bg='forest green',fg='red',command=display_credits,width=10,activebackground='lawn green').place(x=1200,y=108)

play_frame=Frame(root,height=700,width=1600,background='lawn green')

display=Label(play_frame,text='Display',font=('Arial',38),bg='lawn green',fg='forest green')
display.place(x=590,y=70)
characteristics=Label(play_frame,text='',font=('Arial',20),bg='lawn green',fg='red')
characteristics.place(x=590,y=200)
entry=Entry(play_frame,font=('Arial',20),width=10)
entry.place(x=600,y=300)
Next=Button(play_frame,text='Next',font=('Arial',16),bg='lawn green',fg='forest green',width=10,command=play_game)
Next.place(x=600,y=400)
turns_label=Label(play_frame,text='Turn:',font=('Arial',16),bg='lawn green',fg='forest green')
turns_label.place(x=300,y=20)
chances_label=Label(play_frame,text='Chances:',font=('Arial',16),bg='lawn green',fg='forest green')
chances_label.place(x=590,y=20)
score_label=Label(play_frame,text='Score:',font=('Arial',16),bg='lawn green',fg='forest green')
score_label.place(x=900,y=20)

word_list=[]
subject=''
obj=''
turns=0
score=0
increment=0
start=0


root.mainloop()

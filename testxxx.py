##import winsound
##
##winsound.PlaySound('Beach_Chill-Out.wav',winsound.SND_ALIAS|winsound.SND_LOOP|winsound.SND_NODEFAULT|winsound.SND_NOSTOP|winsound.SND_ASYNC)
from Tkinter import *

rootA=Tk()
rootA.geometry('500x500+400+100')
rootA.title('Instruction')
w=Listbox(rootA,bg='lawn green',font=('Arial',18))
s='''
A
B
C
D
'''
s=s.split('\n')
for c in range(len(s)):
    w.insert(c+1,s[c])
w.pack(expand=YES,fill=BOTH)

rootA.destroy()
rootA.mainloop()



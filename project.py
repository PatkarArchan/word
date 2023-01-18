from tkinter import*
import random 

root=Tk()
root.geometry("400x400")
root.title("Word")
root.config(background="Yellow")

l1 = Label(root)
l1.place(relx=0.5,rely=0.5,anchor=CENTER)

def word():
    list1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    r1 = random.randint(0,25)
    r2 = random.randint(0,25)
    r3 = random.randint(0,25)
    r4 = random.randint(0,25)
    r5 = random.randint(0,25)
    
    a1 = list1[r1]
    a2 = list1[r2]
    a3 = list1[r3]
    a4 = list1[r4]
    a5 = list1[r5]
    
    l1["text"]=a1+a2+a3+a4+a5
b1 = Button(root,text="Creat An Word",command=word)
b1.place(relx = 0.5,rely = 0.4,anchor=CENTER)
    
root.mainloop()

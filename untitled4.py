from tkinter import*

import random

root=Tk()
root.geometry("400x400")
root.title("Lucky friend")
list1 =["Prajwal","omkar","addi","jay","ved","neel","siddhart"]
print(list1)

def best_friend():
    r1 = random.randint(0,6)
    print(r1)
    lucky_friend  = list1[r1]
    print("Your lucky Friend is: " + lucky_friend)

b1 = Button(root,text="Find Your Lucky Friend",command=best_friend)
b1.place(relx = 0.5,rely = 0.5,anchor=CENTER)

    


root.mainloop()
import random
# import tkinter as tk
from tkinter import *

def secretnumber(mySn):
    num = random.randint(1,mySn)
    return num

if __name__ == '__main__':
    root = Tk()
    root.title('bob')
    root.geometry('500x500')
    frame1 = Frame(root, bg='green')
    frame1.pack(expand=True, fill=BOTH)
    btn1 = Button(frame1, text = "Action", command = root.destroy)
    btn1.pack(side=LEFT)
    root.mainloop()

    mySn = int(input("enter the range for the random number: "))
    sn = secretnumber(mySn)
    goes = 6
    # print(sn) used to know the value
    myguess = int(input("please guess the number: "))
    for i in range(1, goes):
        if (myguess < sn):
            print("too low you have {} goes left".format(goes - i-1))
        elif (myguess > sn):
            print("too high you have {} goes left".format(goes - i-1))
        elif (myguess == sn):
            print("perfect")
            exit()
        i = i+1
        if i != goes:
            myguess = int(input("please another guess at the number: "))
    print("Sorry you had too many goes")
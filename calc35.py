from tkinter import *

# import math
font = ('Consolas', 15)  # ,'bold underline')

window = Tk()
window.title('Calculator')
window.geometry('450x600')
# creating heading
headlabel = Label(window, text='Normal Calculator', fg='red', font=('Consolas', 16, 'bold underline'), justify='center')
headlabel.pack()
# textfield
textfield = Entry(window, font=font, justify=CENTER, relief='solid', width=30)
textfield.pack(pady=10)
# Buttons
# buttonframe=Frame(window)
# buttonframe.pack()
btnexit = Button(window, text="Exit", fg='red', bg='brown', relief=RAISED, command=window.destroy)
btnexit.pack()

window.mainloop()


# add num1 to num2
def add(num1, num2):
    return num1 + num2

# subtract num2 from num1
def subtract(num1, num2):
    return num1 - num2

# divide num1 by num2
def divide(num1, num2):
    return num1 / num2

# Multiply num1 by num2
def multiply(num1, num2):
    return num1 * num2

def main():
    operation = str(input("what operation do you want to do: +, -, /, *, q: "))
    if (operation != '+' and operation != '-' and operation != '/' and operation != '*' and operation != 'q'):
        # invalid operation
        print ("you must enter a valid operation")
        main()
    elif (operation == 'q'):
        print ("goodbye!")
    else:
        var1 = float(input("enter number1: "))
        var2 = float(input("enter number1: "))
        if (operation == '+'):
            print(add(var1, var2))
            main()
        elif (operation == '-'):
            print(subtract(var1, var2))
            main()
        elif (operation == '/'):
            print(divide(var1, var2))
            main()
        elif (operation == '*'):
            print(multiply(var1, var2))
            main()
main()

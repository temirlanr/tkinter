from tkinter import *

root = Tk()
root.title("CalculatOR!!!!")

entry = Entry(root, width=40, borderwidth=3)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current)+str(number))

def clearButton():
    entry.delete(0, END)

def addButton():
    first_number = entry.get()
    global first
    global action
    action = "add"
    first = int(first_number)
    entry.delete(0, END)

def subtractButton():
    first_number = entry.get()
    global first
    global action
    action = "subtract"
    first = int(first_number)
    entry.delete(0, END)

def multiplyButton():
    first_number = entry.get()
    global first
    global action
    action = "multiply"
    first = int(first_number)
    entry.delete(0, END)

def divideButton():
    first_number = entry.get()
    global first
    global action
    action = "divide"
    first = int(first_number)
    entry.delete(0, END)

def equalButton():
    global action
    second_number = entry.get()
    entry.delete(0, END)
    if action == "add":
        entry.insert(0, first + int(second_number))
    elif action == "subtract":
        entry.insert(0, first - int(second_number))
    elif action == "multiply":
        entry.insert(0, first * int(second_number))
    elif action == "divide":
        entry.insert(0, first / int(second_number))


button_0 = Button(root, width=9, text=str(0), pady=10, command=lambda: button_click(0))
button_1 = Button(root, width=9, text=str(1), pady=10, command=lambda: button_click(1))
button_2 = Button(root, width=9, text=str(2), pady=10, command=lambda: button_click(2))
button_3 = Button(root, width=9, text=str(3), pady=10, command=lambda: button_click(3))
button_4 = Button(root, width=9, text=str(4), pady=10, command=lambda: button_click(4))
button_5 = Button(root, width=9, text=str(5), pady=10, command=lambda: button_click(5))
button_6 = Button(root, width=9, text=str(6), pady=10, command=lambda: button_click(6))
button_7 = Button(root, width=9, text=str(7), pady=10, command=lambda: button_click(7))
button_8 = Button(root, width=9, text=str(8), pady=10, command=lambda: button_click(8))
button_9 = Button(root, width=9, text=str(9), pady=10, command=lambda: button_click(9))
button_clear = Button(root, width=9, text="clear", pady=10, command=clearButton, fg="white", bg="grey").grid(row=4, column=0)
button_add = Button(root, width=9, text="+", pady=10, command=addButton).grid(row=1, column=3)
button_equal = Button(root, width=9, text="=", pady=10, command=equalButton).grid(row=4, column=2)
button_subtract = Button(root, width=9, text="-", pady=10, command=subtractButton).grid(row=2, column=3)
button_multiply = Button(root, width=9, text="*", pady=10, command=multiplyButton).grid(row=3, column=3)
button_divide = Button(root, width=9, text="/", pady=10, command=divideButton).grid(row=4, column=3)

# don't judge me...
for i in range(10):
    
    if(i==0):
        globals()["button_"+str(i)].grid(row=4, column=1)
    elif(i==1):
        globals()["button_"+str(i)].grid(row=3, column=0)
    elif(i==2):
        globals()["button_"+str(i)].grid(row=3, column=1)
    elif(i==3):
        globals()["button_"+str(i)].grid(row=3, column=2)
    elif(i==4):
        globals()["button_"+str(i)].grid(row=2, column=0)
    elif(i==5):
        globals()["button_"+str(i)].grid(row=2, column=1)
    elif(i==6):
        globals()["button_"+str(i)].grid(row=2, column=2)
    elif(i==7):
        globals()["button_"+str(i)].grid(row=1, column=0)
    elif(i==8):
        globals()["button_"+str(i)].grid(row=1, column=1)
    elif(i==9):
        globals()["button_"+str(i)].grid(row=1, column=2)


root.mainloop()
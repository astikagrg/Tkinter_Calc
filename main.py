from tkinter import *


# displays string in entry

def disp(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))  # adding two strings


# equals to function

def button_equal():
    cal = str(e.get())  # store value of entry in cal
    total = eval(cal)  # runs the python which is passed as an argument
    e.delete(0, END)  # delete the value in entry
    e.insert(0, total)  # inserts the value in entry


def clear_but():
    e.delete(0, END)  # clears the entry in the screen


root = Tk()
root.configure(bg='black')
root.title('Simple Calculator')

# Defining the buttons

button_1 = Button(root, text='1', command=lambda : button_click(1), font=('Helvetica', 30),fg='lawn green',bg='black', )
button_2 = Button(root, text='2', command=lambda : button_click(2), font=('Helvetica', 30), fg='lawn green', bg='black',)
button_3 = Button(root, text='3', command=lambda : button_click(3), font=('Helvetica', 30),fg='lawn green', bg='black',)
button_4 = Button(root, text='4', command=lambda : button_click(4), font=('Helvetica', 30), fg='lawn green',
    bg='black',
    )
button_5 = Button(
    root,
    text='5',
    command=lambda : button_click(5),
    font=('Helvetica', 30),
    fg='lawn green',
    bg='black',
    )
button_6 = Button(
    root,
    text='6',
    command=lambda : button_click(6),
    font=('Helvetica', 30),
    fg='lawn green',
    bg='black',
    )
button_7 = Button(
    root,
    text='7',
    command=lambda : button_click(7),
    font=('Helvetica', 30),
    fg='lawn green',
    bg='black',
    )
button_8 = Button(
    root,
    text='8',
    command=lambda : button_click(8),
    font=('Helvetica', 30),
    fg='lawn green',
    bg='black',
    )
button_9 = Button(
    root,
    text='9',
    command=lambda : button_click(9),
    font=('Helvetica', 30),
    fg='lawn green',
    bg='black',
)

root.mainloop()

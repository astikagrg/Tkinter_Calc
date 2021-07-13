from tkinter import *
from _ast import Lambda
root = Tk()
root.configure(bg='black')

#to insert an icon
root.iconbitmap('C:/Users/buddha/Desktop/astika/softwarica/lab/cal.ico')

# defining title of the project
root.title('Simple Calculator')

# Function for equals to
def button_eq():
    val = str(e.get())  # converts the value of entry to string and stores it
    ans = eval(val)  # evaluates the answer of value stored in val
    e.delete(0, END)   # deletes the value in entry
    e.insert(0, ans)  # inserts the value of ans in entry

e = Entry(root, width=20, borderwidth=10, font=('Gungsuh', 30), fg='hot pink', bg='black', )
e.grid(row=0, column=0, columnspan=5, padx=15, pady=25, ipadx=10, ipady=10,)

# function to display values that have been clicked
def button_cal(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))



# function to clear the screen
def button_clear():
    e.delete(0, END)  # clears the entry in the screen




# Defining the buttons
button_0 = Button(root, text='0', command=lambda : button_cal(0), font=('Gungsuh', 30),fg='lawn green',bg='black', )
button_1 = Button(root, text='1', command=lambda : button_cal(1), font=('Gungsuh', 30),fg='lawn green',bg='black', )
button_2 = Button(root, text='2', command=lambda : button_cal(2), font=('Gungsuh', 30), fg='lawn green', bg='black',)
button_3 = Button(root, text='3', command=lambda : button_cal(3), font=('Gungsuh', 30),fg='lawn green', bg='black',)
button_4 = Button(root, text='4', command=lambda : button_cal(4), font=('Gungsuh', 30), fg='lawn green', bg='black',)
button_5 = Button(root, text='5', command=lambda : button_cal(5), font=('Gungsuh', 30), fg='lawn green', bg='black', )
button_6 = Button(root, text='6', command=lambda : button_cal(6), font=('Gungsuh', 30), fg='lawn green', bg='black', )
button_7 = Button(root, text='7', command=lambda : button_cal(7), font=('Gungsuh', 30), fg='lawn green', bg='black', )
button_8 = Button(root, text='8', command=lambda : button_cal(8), font=('Gungsuh', 30), fg='lawn green', bg='black', )
button_9 = Button(root, text='9', command=lambda : button_cal(9), font=('Gungsuh', 30), fg='lawn green', bg='black',)
button_dec = Button(root, text='.', command=lambda : button_cal('.'), font=('Gungsuh', 30),fg='lawn green',bg='black', )
button_add = Button(root, text='+', command=lambda : button_cal('+'), font=('Gungsuh', 30), fg='lawn green', bg='black',)
button_sub = Button(root, text='-', command=lambda : button_cal('-'), font=('Gungsuh', 30), fg='lawn green', bg='black',)
button_mul = Button(root, text='X', command=lambda : button_cal('*'), font=('Gungsuh', 30), fg='lawn green', bg='black',)
button_div = Button(root, text='/', command=lambda : button_cal('/'), font=('Gungsuh', 30), fg='lawn green', bg='black',)
button_exp = Button(root, text='^', command=lambda : button_cal('**'), font=('Gungsuh', 30), fg='lawn green', bg='black',)
button_mod = Button(root, text='mod', command=lambda : button_cal('%'), font=('Gungsuh', 20), fg='lawn green', bg='black',)
button_equ = Button(root, text='=', command=button_eq, font=('Gungsuh', 30), fg='lawn green', bg='black',)
button_clear = Button(root, text='clear', command=button_clear, font=('Gungsuh', 20), fg='lawn green', bg='black',)


button_9.grid(row=1, column=0, ipadx=40, ipady=20)
button_8.grid(row=1, column=1, ipadx=40, ipady=20)
button_7.grid(row=1, column=2, ipadx=40, ipady=20)
button_clear.grid(row=1, column=3, ipadx=19, ipady=31)
button_6.grid(row=2, column=0, ipadx=40, ipady=20)
button_5.grid(row=2, column=1, ipadx=40, ipady=20)
button_4.grid(row=2, column=2, ipadx=40, ipady=20)
button_mul.grid(row=2, column=3, ipadx=40, ipady=20)
button_3.grid(row=3, column=0, ipadx=40, ipady=20)
button_2.grid(row=3, column=1, ipadx=40, ipady=20)
button_1.grid(row=3, column=2, ipadx=40, ipady=20)
button_div.grid(row=3, column=3, ipadx=46, ipady=20)
button_0.grid(row=4, column=0, ipadx=40, ipady=20)
button_dec.grid(row=4, column=1, ipadx=46, ipady=20)
button_add.grid(row=4, column=2, ipadx=40, ipady=20)
button_sub.grid(row=4, column=3, ipadx=37, ipady=20)
button_mod.grid(row=5, column=0, ipadx=29, ipady=30)
button_exp.grid(row=5, column=1, ipadx=41, ipady=20)
button_equ.grid(row=5, column=2,columnspan=2, ipadx=112, ipady=20)

root.mainloop()

"""
Code written by : @Vansh-Coder on Github
Note : This could is licensed under the MIT License. Happy Coding ! :)
"""

from tkinter import *
from tkinter import messagebox

calc = Tk()
calc.title('Calculator')

e = Entry(calc, width=58, borderwidth=3)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
op_list = ('+', '–', '⨯', '÷')

def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(num))

def point():
    if len(e.get()) == 0 or e.get()[-1] in op_list:
        click('0.')
    else:
        x = ''
        for i in e.get()[::-1]:
            if i in op_list:
                break
            x += i
        if x.count('.') == 0:
            click('.')

def clear():
    e.delete(0, END)

def operation(op):
    if len(e.get()) != 0:
        if e.get()[-1] in op_list:
            current = e.get()[:-1]
            e.delete(0, END)
            e.insert(0, current + op)
        else:
            click(op)

def equal():
    f = False
    if len(e.get()) == 0:
        f = True
    for i in e.get():
        if i.isdigit() is False and i not in op_list and i != '.':
            f = True
            messagebox.showinfo("Invalid Expression Error !", 'The expression "' + e.get() + '" is invalid, try again with a valid expression.')
            e.delete(0, END)
            break
    if f is False:
        if e.get()[-1] in op_list:
            messagebox.showinfo("Invalid Expression Error !", 'The expression "' + e.get() + '" is invalid, try again with a valid expression.')
            e.delete(0, END)
        else:
            try:
                current = e.get()
                current = current.replace('–', '-').replace('⨯', '*').replace('÷', '/')
                result = str(eval(current))
                if len(result) >= 3 and result[-2] == '.' and result[-1] == '0':
                    result = result[:-2]
                e.delete(0, END)
                e.insert(0, result)
            except ZeroDivisionError:
                messagebox.showinfo("Undefined Expression Error !", 'The expression "' + e.get() + '" is invalid as it contains division by zero which is undefined. Try again with a valid expression.')
                e.delete(0, END)

def backspace():
    current = e.get()[:len(e.get())-1]
    e.delete(0, END)
    e.insert(0, current)

button_1 = Button(calc, text='1', padx=40, pady=20, activebackground='#cccccc', command=lambda: click(1))
button_2 = Button(calc, text='2', padx=40, pady=20, activebackground='#cccccc', command=lambda: click(2))
button_3 = Button(calc, text='3', padx=40, pady=20, activebackground='#cccccc', command=lambda: click(3))
button_4 = Button(calc, text='4', padx=40, pady=20, activebackground='#cccccc', command=lambda: click(4))
button_5 = Button(calc, text='5', padx=40, pady=20, activebackground='#cccccc', command=lambda: click(5))
button_6 = Button(calc, text='6', padx=40, pady=20, activebackground='#cccccc', command=lambda: click(6))
button_7 = Button(calc, text='7', padx=40, pady=20, activebackground='#cccccc', command=lambda: click(7))
button_8 = Button(calc, text='8', padx=40, pady=20, activebackground='#cccccc', command=lambda: click(8))
button_9 = Button(calc, text='9', padx=40, pady=20, activebackground='#cccccc', command=lambda: click(9))
button_0 = Button(calc, text='0', padx=40, pady=20, activebackground='#cccccc', command=lambda: click(0))

button_point = Button(calc, text='.', width=1, padx=40, pady=20, activebackground='#cccccc', command=point)
button_equal = Button(calc, text='=', padx=39, pady=20, activebackground='#cccccc', command=equal)
button_add = Button(calc, text='+', padx=37, pady=20, width=2, activebackground='#cccccc', command=lambda: operation('+'))
button_subtract = Button(calc, text='–', padx=37, pady=20, width=2, activebackground='#cccccc', command=lambda: operation('–'))
button_multiply = Button(calc, text='⨯', padx=39, pady=20, activebackground='#cccccc', command=lambda: operation('⨯'))
button_divide = Button(calc, text='÷', padx=37, pady=20, width=2, activebackground='#cccccc', command=lambda: operation('÷'))
button_backspace = Button(calc, text='⌫', padx=40, pady=20, width=1, fg='#ff3333', activeforeground='#ff1a1a', activebackground='#cccccc', command=backspace)
button_clear = Button(calc, text='Clear All', padx=40, pady=20, width=1, fg='#ff3333', activeforeground='#ff1a1a', activebackground='#cccccc', command=clear)
button_exit = Button(calc, text='Exit', padx=39, pady=20, width=15, fg='#ff3333', activeforeground='#ff1a1a', activebackground='#cccccc', command=calc.destroy)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_point.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_backspace.grid(row=5, column=0)
button_clear.grid(row=5, column=1)
button_exit.grid(row=5, column=2, columnspan=2)

calc.resizable(False, False)
calc.mainloop()

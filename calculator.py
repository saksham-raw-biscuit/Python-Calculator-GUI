import tkinter
from tkinter import *
from tkinter import ttk
    
    
mainscreen = Tk()

mainscreen.title("Calcualtor")
# mainscreen.geometry('320x321')
mainscreen.resizable(0,0)

global i
i = 0
text="hello"



input_field = Entry(mainscreen)
# input_field.pack()
input_field.grid(row = 1,columnspan=7)

def clear_all():
    new_field = input_field.delete(0,tkinter.END)
    input_field.insert(0,new_field)


def get_number(value):
    global i
    print(i)
    input_field.insert(i,value)
    i += 1

def get_operator(value):
    global i
    print(i)
    length = len(value)
    input_field.insert(i,value)
    i += length

#first row
seven = Button(mainscreen,text = "7",width = 9,command=lambda : get_number('7'),activebackground="grey", activeforeground="black",padx=8,pady=5)
seven.grid(row = 2, column = 2)

eight = Button(mainscreen,text = "8",width = 9,command=lambda : get_number('8') ,activebackground="grey", activeforeground="black",padx=8,pady=5)
eight.grid(row = 2, column = 3)

nine = Button(mainscreen,text = "9",width = 9,command=lambda : get_number('9'),activebackground="grey", activeforeground="black",padx=8,pady=5)
nine.grid(row = 2, column = 4)

plus = Button(mainscreen,text = "+",width = 9,command=lambda : get_operator('+'),activebackground="grey", activeforeground="black",padx=8,pady=5)
plus.grid(row = 2, column = 5)

factorial = Button(mainscreen,text = "x!",width = 9,command=lambda : get_factorial('!'),activebackground="grey", activeforeground="black",padx=8,pady=5)
factorial.grid(row = 2, column = 6)

#second row
four = Button(mainscreen,text = "4",width = 9,command=lambda : get_number('4'),activebackground="grey", activeforeground="black",padx=8,pady=5)
four.grid(row = 3, column = 2)

five = Button(mainscreen,text = "5",width = 9,command=lambda : get_number('5'),activebackground="grey", activeforeground="black",padx=8,pady=5)
five.grid(row = 3, column = 3)

six = Button(mainscreen,text = "6",width = 9,command=lambda : get_number('6'),activebackground="grey", activeforeground="black",padx=8,pady=5)
six.grid(row = 3, column = 4)

subtract = Button(mainscreen,text = "-",width = 9,command=lambda : get_operator('-'),activebackground="grey", activeforeground="black",padx=8,pady=5)
subtract.grid(row = 3, column = 5)

left_bracket = Button(mainscreen,text = "(",width = 9,command=lambda : get_operator(')'),activebackground="grey", activeforeground="black",padx=8,pady=5)
left_bracket.grid(row = 3, column = 6)

#third row
one = Button(mainscreen,text = "1",width = 9,command=lambda : get_number('1'),activebackground="grey", activeforeground="black",padx=8,pady=5)
one.grid(row = 4, column = 2)

two = Button(mainscreen,text = "2",width = 9,command=lambda : get_number('2'),activebackground="grey", activeforeground="black",padx=8,pady=5)
two.grid(row = 4, column = 3)

three = Button(mainscreen,text = "3",width = 9,command=lambda : get_number('3'),activebackground="grey", activeforeground="black",padx=8,pady=5)
three.grid(row = 4, column = 4)

multiply = Button(mainscreen,text = "x",width = 9,command=lambda : get_operator('*'),activebackground="grey", activeforeground="black",padx=8,pady=5)
multiply.grid(row = 4, column = 5)

left_bracket = Button(mainscreen,text = ")",width = 9,command=lambda : get_operator(')'),activebackground="grey", activeforeground="black",padx=8,pady=5)
left_bracket.grid(row = 4, column = 6)


#fourt row
clear = Button(mainscreen,text = "AC",width = 9,command=lambda : clear_all(),activebackground="grey", activeforeground="black",padx=8,pady=5)
clear.grid(row = 5, column = 2)

zero = Button(mainscreen,text = "0",width = 9,command=lambda : get_number('0'),activebackground="grey", activeforeground="black",padx=8,pady=5)
zero.grid(row = 5, column = 3)

equal = Button(mainscreen,text = "=",width = 9,command=lambda : get_number(),activebackground="grey", activeforeground="black",padx=8,pady=5)
equal.grid(row = 5, column = 4)

divide = Button(mainscreen,text = "/",width = 9,command=lambda : get_operator('/'),activebackground="grey", activeforeground="black",padx=8,pady=5)
divide.grid(row = 5, column = 5)

square = Button(mainscreen,text = "^2",width = 9,command=lambda : get_operator('**2'),activebackground="grey", activeforeground="black",padx=8,pady=5)
square.grid(row = 5, column = 6)





mainscreen.mainloop()

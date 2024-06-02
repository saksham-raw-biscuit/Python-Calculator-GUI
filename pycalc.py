import tkinter as tk
from tkinter import ttk
from tkinter import *
"""
Importing all the necessary liraries and tool Kit. This program anly consist of the tknter and its related widgets.
"""

class CalcGUI:

    FONT_MEDIUM = ('Calibre',10)
    FONT_MEDIUM = ('Calibre',7)

    global i 
    i=0

    used=['s']

    def __init__(self):  # As usual calling the init constructor
        """
        THe main basic property are defined here
        """
        try:
            super().__init__() # super constructor is defined, Super/Tk class is always called
                                #if we had used other parameter in the CalcGUI class then the super would ahve been perplace as tkinter.name.__init__(self)
        except TypeError:
            tk.Tk.__init__(self)

        self.screen = Tk()

            

        self.screen.resizable(0,0)
        self.screen.title("Calculator")

        thm = ttk.Style()
        thm.theme_use('clam')

        self.input_field = Entry(self.screen)
        self.input_field.grid(row =0 , columnspan= 6)
        # self.input_field.grid(ipadx=5)
        self.OnHover(self.input_field, "red", "gray")

        #Giving the tkinter app an new icon, reolacing the feather from tkinter
        icon_ = tk.PhotoImage(file='icon.png')
        self.screen.wm_iconphoto(False,icon_)
        # self.overrideredirect(True) # to create a frameless screen.

        self.__init_interface()

    def __init_interface(self):



        #first row
        self.seven = tk.Button(
            self.screen,text = "7",width = 9,command=lambda : self.get_number('7'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        self.seven.grid(row = 2, column = 2 )

        eight = Button(
            self.screen,text = "8",width = 9,command=lambda : self.get_number('8') ,activebackground="grey", activeforeground="black",padx=8,pady=5)
        eight.grid(row = 2, column = 3)

        nine = Button(self.screen,text = "9",width = 9,command=lambda : self.get_number('9'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        nine.grid(row = 2, column = 4)

        plus = Button(self.screen,text = "+",width = 9,command=lambda : self.get_operator('+'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        plus.grid(row = 2, column = 5)

        factorial = Button(self.screen,text = "x!",width = 9,command=lambda : self.get_factorial(),activebackground="grey", activeforeground="black",padx=8,pady=5)
        factorial.grid(row = 2, column = 6)
        self.OnHover(factorial, "red", "yellow")

        #second row
        four = Button(self.screen,text = "4",width = 9,command=lambda : self.get_number('4'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        four.grid(row = 3, column = 2)

        five = Button(self.screen,text = "5",width = 9,command=lambda : self.get_number('5'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        five.grid(row = 3, column = 3)

        six = Button(self.screen,text = "6",width = 9,command=lambda : self.get_number('6'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        six.grid(row = 3, column = 4)

        subtract = Button(self.screen,text = "-",width = 9,command=lambda : self.get_operator('-'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        subtract.grid(row = 3, column = 5)

        left_bracket = Button(self.screen,text = "(",width = 9,command=lambda : self.get_operator('('),activebackground="grey", activeforeground="black",padx=8,pady=5)
        left_bracket.grid(row = 3, column = 6)

        #third row
        one = Button(self.screen,text = "1",width = 9,command=lambda : self.get_number('1'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        one.grid(row = 4, column = 2)

        two = Button(self.screen,text = "2",width = 9,command=lambda : self.get_number('2'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        two.grid(row = 4, column = 3)

        three = Button(self.screen,text = "3",width = 9,command=lambda : self.get_number('3'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        three.grid(row = 4, column = 4)

        multiply = Button(self.screen,text = "x",width = 9,command=lambda : self.get_operator('*'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        multiply.grid(row = 4, column = 5)

        left_bracket = Button(self.screen,text = ")",width = 9,command=lambda : self.get_operator(')'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        left_bracket.grid(row = 4, column = 6)


        #fourt row
        clear = Button(self.screen,text = "AC",width = 9,command=lambda : self.clear_all_expression   (),activebackground="grey", activeforeground="black",padx=8,pady=5,foreground = "Red")
        clear.grid(row = 5, column = 2)

        zero = Button(self.screen,text = "0",width = 9,command=lambda : self.get_number('0'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        zero.grid(row = 5, column = 3)

        equal = Button(self.screen,text = "=",width = 9,command=lambda : self.get_calculation(),activebackground="grey", activeforeground="black",padx=8,pady=5)
        equal.grid(row = 5, column = 4)

        divide = Button(self.screen,text = "/",width = 9,command=lambda : self.get_operator('/'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        divide.grid(row = 5, column = 5)

        square = Button(self.screen,text = "^2",width = 9,command=lambda : self.get_number('**2'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        square.grid(row = 5, column = 6)
            
        # self.run()

    def OnHover (self,widget,hoverColor,leaveColor):

        widget.bind("<Enter>", func=lambda e: widget.config (background = hoverColor))
        widget.bind("<Leave>", func=lambda e: widget.config(background = leaveColor))   






    def get_factorial(self):
        """Calculates the factorial of the number entered."""
        global i

        num = int(self.input_field.get())
        fact = 1 

        try:
            while num > 0:
                fact = fact*num
                num -= 1
            self.clear_all_expression()
            self.input_field.insert(0, fact)
            i = len(self.input_field.get())

        except Exception:
            self.clear_all_expression()
            self.input_field.insert(0, "Error")

    def clear_all_expression(self):
        global i
        new_field = self.input_field.delete(0,END)
        print("Cleared all")
        self.input_field.insert(i,'')


    def get_calculation(self):
        global i
        try:
            # used = used.clear()
            expression = self.input_field.get()
            ans = eval(expression)
            self.input_field.delete(0,END)
            self.input_field.insert(0,ans)
            i = len(self.input_field.get())
        except SyntaxError:
            # self.used = self.used.clear()
            self.input_field.delete(0,END)
            self.input_field.insert(i,"Invalid Syntax")
            raise SyntaxError ("Use proper equation you sick")

            
    def get_number(self,value):
        global i
        field = self.input_field.get()
        if field == "Invalid Syntax" or value == "Error":
            self.input_field.delete(0,END)
            self.input_field.insert(0,value)
            i += 1
        else:
            self.input_field.insert(i,value)
            i += 1

    def get_operator(self,value):
        global i
        # print(i)
        field = self.input_field.get()
        length = len(value)

        if field == "Invalid Syntax" or value == "Error":
            self.input_field.delete(0,END)
            self.input_field.insert(0,value)
            i += length
        else:
            self.input_field.insert(i,value)
            i += length
    


    def loop(self):
        self.screen.mainloop()

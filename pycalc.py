import tkinter
from tkinter import ttk
from tkinter import *
"""
Importing all the necessary liraries and tool Kit. This program anly consist of the tknter and its related widgets.
"""

class CalcGUI(tkinter.Tk):

    FONT_MEDIUM = ('Calibre',10)
    FONT_MEDIUM = ('Calibre',7)

    global i 
    i=0

    def __init__(self):  # As usual calling the init constructor
        """
        THe main basic property are defined here
        """
        super().__init__() # super constructor is defined, Super/Tk class is always called
                                #if we had used other parameter in the CalcGUI class then the super would ahve been perplace as tkinter.name.__init__(self)
        # self.screen = Tk()
        self.resizable(width=False,height=False)
        self.title("Calculator")


        self.geometry("312x321")

        thm = ttk.Style()
        thm.theme_use('clam')

        self.input_field = tkinter.Entry(self,width = 312)
        self.input_field.grid(column = 0, row =0 )
        self.input_field.grid(ipady=5)

        #Giving the tkinter app an new icon, reolacing the feather from tkinter
        icon_ = tkinter.PhotoImage(file='icon.png')
        self.wm_iconphoto(False,icon_)

        self.__init_ui()

    def __init_ui(self):

        #first row
        seven = Button(self,text = "7",width = 9,command=lambda : self.get_number('7'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        seven.grid(row = 2, column = 2)

        eight = Button(self,text = "8",width = 9,command=lambda : self.get_number('8') ,activebackground="grey", activeforeground="black",padx=8,pady=5)
        eight.grid(row = 2, column = 3)

        nine = Button(self,text = "9",width = 9,command=lambda : self.get_number('9'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        nine.grid(row = 2, column = 4)

        plus = Button(self,text = "+",width = 9,command=lambda : self.get_operator('+'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        plus.grid(row = 2, column = 5)

        factorial = Button(self,text = "x!",width = 9,command=lambda : self.get_factorial('!'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        factorial.grid(row = 2, column = 6)
        # self.OnHover(factorial, "red", "yellow")

        #second row
        four = Button(self,text = "4",width = 9,command=lambda : self.get_number('4'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        four.grid(row = 3, column = 2)

        five = Button(self,text = "5",width = 9,command=lambda : self.get_number('5'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        five.grid(row = 3, column = 3)

        six = Button(self,text = "6",width = 9,command=lambda : self.get_number('6'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        six.grid(row = 3, column = 4)

        subtract = Button(self,text = "-",width = 9,command=lambda : self.get_operator('-'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        subtract.grid(row = 3, column = 5)

        left_bracket = Button(self,text = "(",width = 9,command=lambda : self.get_operator('('),activebackground="grey", activeforeground="black",padx=8,pady=5)
        left_bracket.grid(row = 3, column = 6)

        #third row
        one = Button(self,text = "1",width = 9,command=lambda : self.get_number('1'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        one.grid(row = 4, column = 2)

        two = Button(self,text = "2",width = 9,command=lambda : self.get_number('2'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        two.grid(row = 4, column = 3)

        three = Button(self,text = "3",width = 9,command=lambda : self.get_number('3'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        three.grid(row = 4, column = 4)

        multiply = Button(self,text = "x",width = 9,command=lambda : self.get_operator('*'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        multiply.grid(row = 4, column = 5)

        left_bracket = Button(self,text = ")",width = 9,command=lambda : self.get_operator(')'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        left_bracket.grid(row = 4, column = 6)


        #fourt row
        clear = Button(self,text = "AC",width = 9,command=lambda : self.clear_all_expression   (),activebackground="grey", activeforeground="black",padx=8,pady=5,foreground = "Red")
        clear.grid(row = 5, column = 2)

        zero = Button(self,text = "0",width = 9,command=lambda : self.get_number('0'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        zero.grid(row = 5, column = 3)

        equal = Button(self,text = "=",width = 9,command=lambda : self.get_calculation(),activebackground="grey", activeforeground="black",padx=8,pady=5)
        equal.grid(row = 5, column = 4)

        divide = Button(self,text = "/",width = 9,command=lambda : self.get_operator('/'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        divide.grid(row = 5, column = 5)

        square = Button(self,text = "^2",width = 9,command=lambda : self.get_number('**2'),activebackground="grey", activeforeground="black",padx=8,pady=5)
        square.grid(row = 5, column = 6)
            
        self.run()

    def OnHover (self,widget,hoverColor,leaveColor):

        widget.bind("<Enter>", func=lambda e: widget.config (background = hoverColor))
        widget.bind("<Leave>", func=lambda e: widget.config(background = leaveColor))   



    # get_factorial():

    def get_factorial(self,operator):
        """Calculates the factorial of the number entered."""
        number = int(self.input_field.get())
        fact = 1
        try:
            while number > 0:
                fact = fact*number
                number -= 1
            self.clear_all_expression()
            self.input_field.insert(0, fact)
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
            expression = self.input_field.get()
            ans = eval(expression)
            self.input_field.delete(0,END)
            self.input_field.insert(0,ans)
        except SyntaxError:
            self.input_field.delete(0,END)
            self.input_field.insert(i,"Invalid Syntax")
            raise SyntaxError ("Use proper equation you sick")

            
    def get_number(self,value):
        global i
        # print(i)
        self.input_field.insert(i,value)
        i += 1

    def get_operator(self,value):
        global i
        # print(i)
        length = len(value)
        self.input_field.insert(self.i,value)
        i += length

    def run(self):
        self.mainloop()


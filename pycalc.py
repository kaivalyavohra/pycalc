#Kaivalya Vohra 2019

#importing tkinter library
import tkinter

#create class that inherits from Frame
class CalcFrame(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self)
        #set title
        root.title('Calculator')

        #set up textfield/calculator display
        self.entryText = tkinter.StringVar()
        self.e = tkinter.Entry(root, textvariable=self.entryText, width=37,bd=12)
        self.e.grid(row=0, column=0, columnspan=3)
        #set up buttons
        ac = tkinter.Button(root, text='AC', command=lambda: self.entryText.set(
            ""), padx=50, pady=12, width=2).grid(row=0, column=3)
        buttons = ['789+', '456-', '123*', '0=^/']
        col, row = 0, 1
        for i in buttons:
            for j in i:
                if j != '^' and j != '=':
                    B=tkinter.Button(root,text=j,command=lambda j=j:self.update(
                        j), padx=50, pady=12, width=2).grid(row=row,column=col)
                #special function for power symbol as ^ becomes **
                elif j == '^':
                    B = tkinter.Button(root, text=j, command=lambda: self.update(
                        '**'), padx=50, pady=12, width=2).grid(row=row, column=col)
                else:
                    #compute every time = is pressed
                    B = tkinter.Button(root, text=j, command=lambda: self.calc(
                    ), padx=50, pady=12, width=2).grid(row=row, column=col)
                col += 1

            row += 1
            col = 0
    #add number/operation to display when pressed
    def update(self, val):
        self.entryText.set(self.e.get() + val)
    #compute
    def calc(self):
        self.entryText.set(eval(self.e.get()))


root = tkinter.Tk()
calc = CalcFrame(root)
root.mainloop()

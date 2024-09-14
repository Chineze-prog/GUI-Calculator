import tkinter
from KeyPad import KeyPad 

calculation = ""

def addToCalculation(symbol):
    pass

def evaluateCalculation():
    pass

def clear():
    pass

root = tkinter.Tk()
root.geometry("325x550")
root.title("Calculator")
root.resizable(False, False)
root.configure(background = "#202020") #dark grey background

keypad = KeyPad(root)
keypad.pack(fill = "both", side = "bottom", pady = (15, 0))
root.mainloop()
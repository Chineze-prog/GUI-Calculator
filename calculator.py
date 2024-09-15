import tkinter as tk
from KeyPad import KeyPad
from CalculationScreen import CalculatorScreen 

calculation = ""

def addToCalculation(symbol):
    pass

def evaluateCalculation():
    pass

def clear():
    pass

root = tk.Tk()
root.geometry("325x550")
root.title("Calculator")
root.resizable(False, False)
root.configure(background = "#202020") #dark grey background

keypad = KeyPad(root)
keypad.pack(fill = "both", side = "bottom", pady = (15, 0))

calculationScreen = CalculatorScreen(root)
calculationScreen.pack(fill = "x", side = "bottom")

root.mainloop()
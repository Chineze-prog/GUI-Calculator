import tkinter as tk
from KeyPad import KeyPad
from CalculationScreen import CalculatorScreen 

root = tk.Tk()
root.geometry("325x550")
root.title("Calculator")
root.resizable(False, False)
root.configure(background = "#202020") # dark grey background

calculationScreen = CalculatorScreen(root)
keypad = KeyPad(root, calculationScreen)

keypad.pack(fill = "both", side = "bottom", pady = (15, 0))
calculationScreen.pack(fill = "x", side = "bottom")

root.mainloop()
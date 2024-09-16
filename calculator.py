import tkinter as tk
from Calculator.KeyPad import KeyPad
from Calculator.CalculationScreen import CalculatorScreen 

'''
This file initializes the calculator GUI, setting up the main window, calculator screen, and keypad.
It arranges them using "pack" for layout and starts the Tkinter main event loop to handle user interactions.
'''
def main():
    root = tk.Tk() # creates the main window
    root.geometry("325x550") # sets the size of the window
    root.title("Calculator") # sets the window's title
    root.resizable(False, False) # disables the window resizing
    root.configure(background = "#202020") # sets the background color to dark grey

    calculationScreen = CalculatorScreen(root) # creates the scree where calculations will be displayed
    keypad = KeyPad(root, calculationScreen) # creates the keypad

    keypad.pack(fill = "both", side = "bottom", pady = (15, 0)) # adds the keypad to the window at the bottom
    calculationScreen.pack(fill = "x", side = "bottom") # adds the screen at the top

    root.mainloop() #starts the Tkinter event loop
    
if __name__ == "__main__":
    main()
import tkinter as tk

class CalculatorScreen(tk.Message):
    def __init__(self, root):
       super().__init__(master = root, text = 0, background = root.cget("background"), foreground = "white", width = 325, font = ("Arial", 40), anchor = "e", padx = 34, pady = 0) 
       
    def equate(self):
        pass
    
    def addToEquation(self, text):
        operators = ("÷", "×", "-", "+", "=")
    
    def reverseSign(self):
        self["text"] = -int(self.cget("text"))
    
    def reduceFont(self):
        self["font"] = ("Arial", int(self.cget("font")[-2:]) - 3)
        
    def clear(self):
        self.configure(text = 0, font = ("Arial", 40))
        
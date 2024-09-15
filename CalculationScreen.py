import tkinter as tk

class CalculatorScreen(tk.Message):
    def __init__(self, root):
       super().__init__(master = root, text = 0, background = root.cget("background"), foreground = "white", width = 325, font = ("Arial", 40), anchor = "e", padx = 34, pady = 0) 
       self.hasEquated = False
       
    def equate(self):
        try:
            answer = eval(self.cget("text").replace("×", "*").replace("÷", "/").replace("%", "*(1/100)*"))
            self["text"] = answer
            self["font"] = ("Arial", 40)
            self.hasEquated = True
        except:
            self["text"] = "Error"
    
    def getHasEquated(self):
        return self.hasEquated
    
    def resetHasEquated(self):
        self.hasEquated = False
        
    def addToEquation(self, text):
        operators = ("÷", "×", "-", "+", "=")
        equation = self.cget("text")
        
        if "Error" not in equation:
            if equation == "0": 
                self["text"] = text
            elif text in operators and equation[-1:] in operators:
                self["text"] = f"{equation[:-1]}{text}"
            else:
                self["text"] += text
        else:
            self.clearAll()
            self["text"] = text
            
    
    def reverseSign(self):
        self["text"] = -int(self.cget("text"))
    
    def reduceFont(self):
        self["font"] = ("Arial", int(self.cget("font")[-2:]) - 3)
       
    def clearPrev(self): 
        equation = self.cget("text")
        self["text"] = f"{equation[:-1]}"
        
    def clearAll(self):
        self.configure(text = 0, font = ("Arial", 40))
        
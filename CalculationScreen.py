import tkinter as tk

class CalculatorScreen(tk.Message):
    def __init__(self, root):
       super().__init__(master = root, text = 0, background = root.cget("background"), foreground = "white", width = 325, font = ("Arial", 40), anchor = "e", padx = 34, pady = 0) 
       
       self.hasEquated = False
       
    def equate(self):
        try:
            answer = eval(self.cget("text").replace("×", "*").replace("÷", "/"))
            self["text"] = round(answer, 10)
            self["font"] = self.reduceFont() if self.winfo_reqwidth() > 280 else ("Arial", 40)
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
            elif text == "%":
                self.hasEquated = True
                # find the last number in the equation
                index = len(equation) - 1
                sig_dig = 0
                
                while index >= 0 and (equation[index].isdigit() or equation[index] == "."):
                    index -= 1
                    
                    if  equation[index] != ".":
                        sig_dig += 1
                    
                lastNumber = float(equation[index+1:])
                
                percentage = "{:.{}g}".format(lastNumber * 0.01, sig_dig)
                self["text"] = f"{equation[:index+1]}{percentage}"
                
            elif text in operators and equation[-1:] in operators:
                self["text"] = f"{equation[:-1]}{text}"
            else:
                self["text"] += text
        else:
            self.clearAll()
            self["text"] = text
    
    def reverseSign(self):
        self["text"] = -float(self.cget("text"))
    
    def reduceFont(self):
        self["font"] = ("Arial", int(self.cget("font")[-2:]) - 3)
       
    def clearAll(self):
        self.configure(text = 0, font = ("Arial", 40))
        
import tkinter as tk

# call the parent class constructor with specific settings for the calculator screen
class CalculatorScreen(tk.Message):
    def __init__(self, root):
       super().__init__(master = root, text = 0, background = root.cget("background"), foreground = "white", width = 325, font = ("Arial", 40), anchor = "e", padx = 34, pady = 0) 
       
       self.hasEquated = False # Track if the equals button has been pressed
       
       
    # Evaluate the expression and display the result.
    def equate(self):
        try:
            # replace symbols and evaluate the expression
            answer = eval(self.cget("text").replace("×", "*").replace("÷", "/"))
            self["text"] = round(answer, 10) # show the result rounded to 10 decimals
            self["font"] = self.reduceFont() if self.winfo_reqwidth() > 280 else ("Arial", 40)
            self.hasEquated = True  # set flag to indicate that the calculation is done
        except:
            self["text"] = "Error" # handle any errors in the expression
    
    
    # return the status of the equated flag
    def getHasEquated(self):
        return self.hasEquated
    
    
    # reset the equated flag
    def resetHasEquated(self):
        self.hasEquated = False
        
        
    # add a number or operator to the current equation
    def addToEquation(self, text):
        operators = ("÷", "×", "-", "+", "=")
        equation = self.cget("text")
        
        if "Error" not in equation:
            if equation == "0": # if the equation is 0, replace it with the new text
                self["text"] = text
            # handle the percentage calculation
            elif text == "%":
                self.hasEquated = True # mark equation as evaluated
                index = len(equation) - 1 # start from the last character
                sig_dig = 0 # significant digits counter
                
                #find the last number in the equation
                while index >= 0 and (equation[index].isdigit() or equation[index] == "."):
                    index -= 1
                    
                    if  equation[index] != ".":
                        sig_dig += 1
                    
                lastNumber = float(equation[index+1:]) # get the last number in the equation
                
                # calculate percentage and update the equation
                percentage = "{:.{}g}".format(lastNumber * 0.01, sig_dig)
                
                self["text"] = f"{equation[:index+1]}{percentage}"
            # if the last character is an operator and the new input is also an operator, replace the last operator 
            elif text in operators and equation[-1:] in operators:
                self["text"] = f"{equation[:-1]}{text}"
            else:
                # add the new input to the equation
                self["text"] += text
        else:
            # if there was an error, clear the equation and start fresh
            self.clearAll()
            self["text"] = text
    
    
    # reverse the sign of the current number
    def reverseSign(self):
        self["text"] = -float(self.cget("text"))
    
    
    # reduce the fontsize if the content exceeds the screen width
    def reduceFont(self):
        self["font"] = ("Arial", int(self.cget("font")[-2:]) - 3)
       
       
    # clear the screen and reset the fontsize
    def clearAll(self):
        self.configure(text = 0, font = ("Arial", 40))
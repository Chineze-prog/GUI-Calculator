import tkinter as tk

'''
This file defines the KeyPad class, which creates the buttons for the calculator using the "Canvas" widget.
Each button is created with an oval or other shapes, e.g. for zero.
It handles hover effects, button presses, and dynamic button text changes between "AC" (clear all) and "C" (clear entry).
'''

# Inherits from the Canvas widget to create a custom keypad
class KeyPad(tk.Canvas):
    def __init__(self, root, calculationScreen):
        super().__init__(master = root, background = root.cget("background"), highlightthickness = 0, height = 380)  
        
        self.buttons = {} # Dictionary to store button objects for reference
        self.calculationScreen = calculationScreen # reference to the calculation screen
        self.side_operators = ("÷", "×", "-", "+", "=") # defines the side operators of the calculator
        
        upper_operators = ("AC", "+/-", "%") # defines the operators of the first row of the calculator
        text = (7, 8, 9, 4, 5, 6, 1, 2, 3, 0, "", ".") # number and other buttons
        
        # loop to create the keypad layout
        for row in range(5):
            for column in range(4):
                x = 20 + 75 * column
                y = 75 * row
                
                # first row buttons
                if row == 0 and column < 3:
                    button_background = "#D3D3D3" # light gray for upper operators
                    button_text = upper_operators[column]
                # rightmost column (operators)
                elif column == 3:
                    button_background = "#FFC000" # yellow for side operators
                    button_text = self.side_operators[row]
                # number and other buttons
                else:
                    button_background = "#505050"  # dark gray for numbers
                    button_text = text[(row - 1) * 3 + column]
                
                # creates the buttons 
                if button_text != "":
                    # special case to draw the zero button
                    if button_text == 0:
                        arc1 = self.create_arc(x, y, x + 60, y + 60, start = 90, extent = 180, fill = button_background, outline = button_background)
                        arc2 = self.create_arc(x + 75, y, x + 135, y + 60, start = -90, extent = 180, fill = button_background, outline = button_background)
                        rect = self.create_rectangle(x + 30, y, x + 107, y + 60.5, fill = button_background, width = 0)
                    
                        button = "zero_button" # name the zero button
                        
                        # group these shapes together for the zero button
                        self.addtag_withtag(button, arc1)
                        self.addtag_withtag(button, arc2)
                        self.addtag_withtag(button, rect)
                    else:
                        # normal buttons
                        button = self.create_oval(x, y, x + 60, y + 60, fill = button_background, width = 0)                    
                
                # creates the button text    
                text_color = "black" if button_background == "#D3D3D3" else "white" # color depends on the button background
                keyboard_text = self.create_text(x + 30, y + 30, text = button_text, fill = text_color, font = ("Arial", 20))
                
                # add hover effects to buttons and text
                self.hoverColorChange(item = button, button = button, color = button_background)
                self.hoverColorChange(item = keyboard_text, button = button, color = button_background)
                
                # handle empty button text
                button_text = 0 if button_text == "" else button_text
                
                # bind click events to the buttons
                self.tag_bind(button, "<Button-1>", lambda event, text = button_text: self.keyPressed(text))
                self.tag_bind(keyboard_text, "<Button-1>", lambda event, text = button_text: self.keyPressed(text))
                
                # store references to buttons
                self.buttons[button_text] = button
                self.buttons[f"text_{button_text}"] = keyboard_text
                
    
    # change button color when hovering                      
    def hoverColorChange(self, item, button, color):
        if color == "#D3D3D3":
            hover_color = "#BFBFBF"
        elif color == "#FFC000":
            hover_color = "#FFDD57"
        elif color == "#505050":
            hover_color = "#707070"
        else:
            hover_color = "white"
            
        # change color when mouse enters and leaves
        self.tag_bind(item, "<Enter>", lambda event: self.itemconfigure(button, fill = hover_color))
        self.tag_bind(item, "<Leave>", lambda event: self.itemconfigure(button, fill = color))
        
    
    # handles button press events    
    def keyPressed(self, text):  
        if text == "AC": 
            self.setButtonText("AC") # reset button text
            self.calculationScreen.clearAll() # clear the screen
        else:
            if text == "C":
                self.setButtonText("AC") # change C back to AC
                self.calculationScreen.clearAll()
            elif text == "+/-": 
                self.calculationScreen.reverseSign() # reverse the sign of the current value
            elif text == "=":
                self.calculationScreen.equate() # perform the calculation
            else:  
                if text not in self.side_operators and text != "%":
                    if self.calculationScreen.getHasEquated(): 
                        self.calculationScreen.resetHasEquated()
                    elif text == "%":
                        self.calculationScreen.clearAll()
                
                    self.setButtonText("C") # set the button text to "C" after a number is pressed
                    
                self.calculationScreen.addToEquation(str(text)) # add the number or operator to the equation
                
        if self.calculationScreen.winfo_reqwidth() > 325:
            self.calculationScreen.reduceFont() # adjust font size if the text is too long
     
     
    # Change button text from "AC" to "C" or Vice versa       
    def setButtonText(self, text):
        if "AC" in self.buttons:
            self.itemconfigure(self.buttons["text_AC"], text = text)
import tkinter as tk

class KeyPad(tk.Canvas):
    def __init__(self, root, calculationScreen):
        super().__init__(master = root, background = root.cget("background"), highlightthickness = 0, height = 380)  
        
        self.buttons = {}
        self.calculationScreen = calculationScreen
        self.side_operators = ("÷", "×", "-", "+", "=")
        
        upper_operators = ("AC", "+/-", "%")
        text = (7, 8, 9, 4, 5, 6, 1, 2, 3, 0, "", ".")
        
        for row in range(5):
            for column in range(4):
                x = 20 + 75 * column
                y = 75 * row
                
                if row == 0 and column < 3:
                    button_background = "#D3D3D3"
                    button_text = upper_operators[column]
                elif column == 3:
                    button_background = "#FFC000"
                    button_text = self.side_operators[row]
                else:
                    button_background = "#505050"
                    button_text = text[(row - 1) * 3 + column]
                
                if button_text != "":
                    if button_text == 0:
                        arc1 = self.create_arc(x, y, x + 60, y + 60, start = 90, extent = 180, fill = button_background, outline = button_background)
                        arc2 = self.create_arc(x + 75, y, x + 135, y + 60, start = -90, extent = 180, fill = button_background, outline = button_background)
                        rect = self.create_rectangle(x + 30, y, x + 107, y + 60.5, fill = button_background, width = 0)
                    
                        button = "zero_button"
                        
                        self.addtag_withtag(button, arc1)
                        self.addtag_withtag(button, arc2)
                        self.addtag_withtag(button, rect)
                    else:
                        button = self.create_oval(x, y, x + 60, y + 60, fill = button_background, width = 0)                    
                    
                text_color = "black" if button_background == "#D3D3D3" else "white"
                keyboard_text = self.create_text(x + 30, y + 30, text = button_text, fill = text_color, font = ("Arial", 20))
                
                self.hoverColorChange(item = button, button = button, color = button_background)
                self.hoverColorChange(item = keyboard_text, button = button, color = button_background)
                
                button_text = 0 if button_text == "" else button_text
                
                self.tag_bind(button, "<Button-1>", lambda event, text = button_text: self.keyPressed(text))
                self.tag_bind(keyboard_text, "<Button-1>", lambda event, text = button_text: self.keyPressed(text))
                
                self.buttons[button_text] = button
                self.buttons[f"text_{button_text}"] = keyboard_text
                
                          
    def hoverColorChange(self, item, button, color):
        if color == "#D3D3D3":
            hover_color = "#BFBFBF"
        elif color == "#FFC000":
            hover_color = "#FFDD57"
        elif color == "#505050":
            hover_color = "#707070"
        else:
            hover_color = "white"
            
        self.tag_bind(item, "<Enter>", lambda event: self.itemconfigure(button, fill = hover_color))
        self.tag_bind(item, "<Leave>", lambda event: self.itemconfigure(button, fill = color))
        
        
    def keyPressed(self, text):
        if text == "AC": 
            self.setButtonText("AC")
            self.calculationScreen.clearAll()
        else:
            if text == "C":
                self.setButtonText("AC")
                self.calculationScreen.clearAll()
            elif text == "+/-": 
                self.calculationScreen.reverseSign()
            elif text == "=":
                self.calculationScreen.equate()
            else:  
                if text not in self.side_operators and text != "%":
                    if self.calculationScreen.getHasEquated(): 
                        self.calculationScreen.resetHasEquated()
                    elif text == "%":
                        self.calculationScreen.clearAll()
                
                    self.setButtonText("C")
                    
                self.calculationScreen.addToEquation(str(text))
                
        if self.calculationScreen.winfo_reqwidth() > 325:
            self.calculationScreen.reduceFont()
            
    def setButtonText(self, text):
        # Change button text from "AC" to "C" or Vice versa
        if "AC" in self.buttons:
            self.itemconfigure(self.buttons["text_AC"], text = text)
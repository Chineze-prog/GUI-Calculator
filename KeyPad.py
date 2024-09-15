import tkinter as tk
class KeyPad(tk.Canvas):
    def __init__(self, root):
        super().__init__(master = root, background = root.cget("background"), highlightthickness = 0, height = 380)  
        
        upper_operators = ("AC", "+/-", "%")
        side_operators = ("÷", "×", "-", "+", "=")
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
                    button_text = side_operators[row]
                else:
                    button_background = "#505050"
                    button_text = text[(row - 1) * 3 + column]
                
                
                if not button_text in (0, ""):
                    button = self.create_oval(x, y, x + 60, y + 60, fill = button_background, width = 0)
                elif button_text == 0:
                    arc1 = self.create_arc(x, y, x + 60, y + 60, start = 90, extent = 180, fill = button_background, outline = button_background)
                    arc2 = self.create_arc(x + 75, y, x + 135, y + 60, start = -90, extent = 180, fill = button_background, outline = button_background)
                    rect = self.create_rectangle(x + 30, y, x + 107, y + 60.5, fill = button_background, width = 0)
                    
                    self.addtag_withtag("zero_button", arc1)
                    self.addtag_withtag("zero_button", arc2)
                    self.addtag_withtag("zero_button", rect)
                    
                    button = "zero_button"
                    
                text_color = "black" if button_background == "#D3D3D3" else "white"
                keyboard_text = self.create_text(x + 30, y + 30, text = button_text, fill = text_color, font = ("Arial", 20))
                
                self.hoverColorChange(item = button, button = button, color = button_background)
                self.hoverColorChange(item = keyboard_text, button = button, color = button_background)
                
                          
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
        pass
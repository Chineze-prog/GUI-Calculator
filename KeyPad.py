import tkinter
class KeyPad(tkinter.Canvas):
    def __init__(self, root):
        super().__init__(master = root, background = root.cget("background"), highlightthickness = 0, height = 380)  
        
        for row in range(5):
            for column in range(4):
                x = 20 + 75*column
                y = 75*row
                
                if row == 0 and column < 3:
                    button_background = "#D3D3D3"
                elif column == 3:
                    button_background = "#FFC000"
                else:
                    button_background = "#262626"
                    
                button = self.create_oval(x, y, x+60, y+60, fill=button_background, width=0)
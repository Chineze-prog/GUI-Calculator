import unittest 
from Calculator.CalculationScreen import CalculatorScreen
import tkinter as tk

'''
Tests the core functionality of the calculator
'''

class CalculatorScreenTest(unittest.TestCase):
    # setup method that is called at the before each test to create a fresh testing environment
    def setUp(self):
        # creates a Tkinter root window and an instance of CalculatorScreen
        self.root = tk.Tk()
        self.calculator_screen = CalculatorScreen(self.root)
       
    # tear down method that is called after each test to destroy the window and clean up 
    def tearDown(self):
        self.root.destroy()
        
    # testing that the equation is evaluated correctly
    def test_equate(self):
        # simulating entering "5+7" and pressing the equals button
        self.calculator_screen.addToEquation("5")
        self.calculator_screen.addToEquation("+")
        self.calculator_screen.addToEquation("7")
        self.calculator_screen.equate()
        
        #check if the answer in "8"
        self.assertEqual(self.calculator_screen.cget("text"), "12")
    
    def test_add_to_equation(self):
        pass
    
    def test_reverse_sign(self):
        pass
    
    # tests that the screen is cleared correctly
    def test_clear_all(self):
        # simulating entering "269" and pressing the clear button
        self.calculator_screen.addToEquation("269")
        self.calculator_screen.clearAll()

        #check if the screen shows "0"
        self.assertEqual(self.calculator_screen.cget("text"), "0")
    
    
    def test_percentage_conversion(self):
        pass
    
if __name__ == "__main__":
    unittest.main() # run the tests
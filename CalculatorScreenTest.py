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
        
    # testing that 
    
    def test_equate(self):
        pass
    
    def test_add_to_equation(self):
        pass
    
    def test_reverse_sign(self):
        pass
    
    def test_clear_all(self):
        pass
    
    def test_percentage_conversion(self):
        pass
    
    if __name__ == "__main__":
        unittest.main() # run the tests
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
    
    # tests that numbers and operators are properly added to the equation
    def test_add_to_equation(self):
        # simulating adding "5", "+", "7" to the equation
        self.calculator_screen.addToEquation("5")
        self.calculator_screen.addToEquation("+")
        self.calculator_screen.addToEquation("7")
        
        #check if the screen shows "5+7"
        self.assertEqual(self.calculator_screen.cget("text"), "5+7")
    
    # tests that the numbers sign is reversed when the reverse sign button is pressed
    def test_reverse_sign(self):
        # simulating entering "4" and pressing the reverse sign button
        self.calculator_screen.addToEquation("4")
        self.calculator_screen.reverseSign()
        #check if the answer in "-4"
        self.assertEqual(self.calculator_screen.cget("text"), "-4")
        self.calculator_screen.clearAll()
        
        # simulating entering "-10" and pressing the reverse sign button
        self.calculator_screen.addToEquation("-10")
        self.calculator_screen.reverseSign()
        #check if the answer in "10"
        self.assertEqual(self.calculator_screen.cget("text"), "10")
        self.calculator_screen.clearAll()
        
        # simulating entering "-10" and pressing the reverse sign button
        self.calculator_screen.addToEquation("-50.467")
        self.calculator_screen.reverseSign()
        #check if the answer in "50.467"
        self.assertEqual(self.calculator_screen.cget("text"), "50.467")
    
    # tests that the screen is cleared correctly
    def test_clear_all(self):
        # simulating entering "269" and pressing the clear button
        self.calculator_screen.addToEquation("269")
        self.calculator_screen.clearAll()

        #check if the screen shows "0"
        self.assertEqual(self.calculator_screen.cget("text"), "0")
    
    # testing the percentage conversion
    def test_percentage_conversion(self):
        # simulating entering "4" and pressing the percentage button
        self.calculator_screen.addToEquation("4")
        self.calculator_screen.addToEquation("%")
        #check if the answer in "0.04"
        self.assertEqual(self.calculator_screen.cget("text"), "0.04")
        self.calculator_screen.clearAll()
        
        # simulating entering "200" and pressing the percentage button
        self.calculator_screen.addToEquation("200")
        self.calculator_screen.addToEquation("%")
        #check if the answer in "2"
        self.assertEqual(self.calculator_screen.cget("text"), "2")
        self.calculator_screen.clearAll()
        
        # simulating entering "4" and pressing the percentage button
        self.calculator_screen.addToEquation("55.36")
        self.calculator_screen.addToEquation("%")
        #check if the answer in "0.5536"
        self.assertEqual(self.calculator_screen.cget("text"), "0.5536")
    
    
if __name__ == "__main__":
    unittest.main() # run the tests
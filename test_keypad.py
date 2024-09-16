import unittest 
import tkinter as tk
from unittest.mock import patch
from Calculator.KeyPad import KeyPad
from Calculator.CalculationScreen import CalculatorScreen

'''
Tests that the correct m,ethods are invoked when buttons are presses, 
using mocks to simulate behaviour
'''
class KeyPadTest(unittest.TestCase):
    # setup method that is called at the before each test to create a fresh testing environment and GUI components
    def setUp(self):
        # creates a Tkinter root window and an instance of CalculatorScreen and KeyPad
        self.root = tk.Tk()
        self.calculator_screen = CalculatorScreen(self.root)
        self.keypad = KeyPad(self.root, self.calculator_screen)
       
    # tear down method that is called after each test to destroy the window and clean up and GUI elements
    def tearDown(self):
        self.root.destroy()
        
    # Test the pressing of a button and ensure that the correct method is called on the CalculatORScreen
    @patch.object(CalculatorScreen, 'addToEquation') # mock the addToEquation method
    def test_number_pressed(self, mock_add):
        self.keypad.keyPressed(5) # simulate pressing the "5" button
        mock_add.assert_called_with("5") # ensure that addToEquation was called with "1"
    
    # testing that the "AC" button is pressed and the clearAll method is called
    @patch.object(CalculatorScreen, 'clearAll') # mock the addToEquation method
    def test_clear_button(self, mock_clear):
        self.keypad.keyPressed("AC")
        mock_clear.assert_called()
    

if __name__ == "__main__":
        unittest.main() # run the tests
    
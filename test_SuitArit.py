
import unittest
import funcSuitArit
class TestFuncs(unittest.TestCase):

    def test_is_arithmetic_sequence(self):
        self.assertTrue(funcSuitArit.suit_arithm([2, 4, 6, 8, 10]))   
        self.assertTrue(funcSuitArit.suit_arithm([1, 5, 9, 13, 17]))  
        self.assertTrue(funcSuitArit.suit_arithm([3, 0, -3, -6, -9]))  
        self.assertFalse(funcSuitArit.suit_arithm([1, 3, 6, 10, 15]))  
        self.assertFalse(funcSuitArit.suit_arithm([2, 5, 10, 17, 26])) 
        self.assertTrue(funcSuitArit.suit_arithm([]))                


if __name__ == '__main__':
    unittest.main()


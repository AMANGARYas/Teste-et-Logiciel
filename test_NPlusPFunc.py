import unittest
import NPlusPFunc
class TestFuncs(unittest.TestCase):


    def test_min_n(self):
        self.assertEqual(NPlusPFunc.min_n([5, 2, 8, 1, 7], 3), [1, 2, 5])
        self.assertEqual(NPlusPFunc.min_n([10, 20, 30, 40, 50], 2), [10, 20])
        self.assertEqual(NPlusPFunc.min_n([1, 2, 3], 1), [1])
        self.assertEqual(NPlusPFunc.min_n([-5, -2, -8, -1, -7], 4), [-8, -7, -5, -2])
        self.assertEqual(NPlusPFunc.min_n([], 5), [])



        
if __name__ == '__main__':
    unittest.main()


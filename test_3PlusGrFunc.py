
import unittest
import 3PluGrFunc 
class TestFuncs(unittest.TestCase):

    def test_max_three(self):
        self.assertEqual(3PluGrFunc.max_three([5, 2, 8, 1, 7]), [8, 7, 5])
        self.assertEqual(3PluGrFunc.max_three([10, 20, 30, 40, 50]), [50, 40, 30])
        self.assertEqual(3PluGrFunc.max_three([1, 2, 3]), [3, 2, 1])
        self.assertEqual(3PluGrFunc.max_three([-5, -2, -8, -1, -7]), [-1, -2, -5])
        self.assertEqual(3PluGrFunc.max_three([]), [])


if __name__ == '__main__':
    unittest.main()


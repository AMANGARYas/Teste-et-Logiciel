import unittest
from LIFO import LIFO

class TestLIFO(unittest.TestCase):

    def test_push_pop(self):
        lifo = LIFO()
        lifo.push(1)
        lifo.push(2)
        lifo.push(3)

        self.assertEqual(lifo.print_stack(), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()

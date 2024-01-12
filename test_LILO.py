
import unittest
from LILO import LILO

class TestLILO(unittest.TestCase):

    def test_enqueue(self):
        lilo = LILO()

        
        lilo.enqueue(1)
        self.assertEqual(lilo.print_queue(), [1])

        lilo.enqueue(2)
        self.assertEqual(lilo.print_queue(), [1, 2])


        lilo.enqueue(3)
        self.assertEqual(lilo.print_queue(), [1, 2, 3])
        

        lilo.dequeue()
        self.assertEqual(lilo.print_queue(), [2, 3])

      
        lilo.dequeue()
        self.assertEqual(lilo.print_queue(), [3])

        lilo.dequeue()
        self.assertEqual(lilo.print_queue(), [])

        self.assertIsNone(lilo.dequeue())        

if __name__ == '__main__':
    unittest.main()


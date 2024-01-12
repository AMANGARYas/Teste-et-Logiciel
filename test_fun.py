
import unittest
from fun import carre, est_pair, somme_carres_nombres_pairs

class TestFuncs(unittest.TestCase):

    def test_carre(self):
        self.assertEqual(carre(2), 4)
        self.assertEqual(carre(-3), 9)
        self.assertEqual(carre(0), 0)

    def test_est_pair(self):
        self.assertTrue(est_pair(2))
        self.assertTrue(est_pair(-4))
        self.assertFalse(est_pair(3))
        self.assertFalse(est_pair(0))

    def test_somme_carres_nombres_pairs(self):
        self.assertEqual(somme_carres_nombres_pairs([2, 4, 6, 8, 10]), 220)
        self.assertEqual(somme_carres_nombres_pairs([1, 3, 5, 7, 9]), 0)
        self.assertEqual(somme_carres_nombres_pairs([]), 0)
        self.assertIsNone(somme_carres_nombres_pairs(["a", 2, 4, 6]))  
        
if __name__ == '__main__':
    unittest.main()


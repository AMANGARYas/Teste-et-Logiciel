import unittest
from LIFO import LIFO

class TestLIFO(unittest.TestCase):

    def test_push_pop(self):
        lifo = LIFO()
        lifo.push(1)
        lifo.push(2)
        lifo.push(3)

        self.assertEqual(lifo.pop(), 3, "Le dernier élément ajouté doit être le premier retiré")
        self.assertEqual(lifo.pop(), 2, "Le deuxième élément ajouté doit être le deuxième retiré")
        self.assertEqual(lifo.pop(), 1, "Le premier élément ajouté doit être le troisième retiré")
        self.assertIsNone(lifo.pop(), "La pile doit être vide après tous les défilements")

    def test_is_empty(self):
        lifo = LIFO()
        self.assertTrue(lifo.is_empty(), "La pile doit être vide au début")

        lifo.push(1)
        self.assertFalse(lifo.is_empty(), "La pile ne doit pas être vide après l'enfilement")

        lifo.pop()
        self.assertTrue(lifo.is_empty(), "La pile doit être vide après le défilement")

if __name__ == '__main__':
    unittest.main()


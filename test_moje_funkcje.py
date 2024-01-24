import unittest
from moje_funkcje import dodaj_liczby, odejmij_liczby

class TestMojeFunkcje(unittest.TestCase):

    def test_dodaj_liczby(self):
        self.assertEqual(dodaj_liczby(2, 3), 5)
        self.assertEqual(dodaj_liczby(-1, 1), 0)

    def test_odejmij_liczby(self):
        self.assertEqual(odejmij_liczby(5, 2), 3)
        self.assertEqual(odejmij_liczby(0, 3), -3)

if __name__ == '__main__':
    unittest.main()

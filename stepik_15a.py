
def iloczyn(a, b):
    return a * b

def suma(a, b):
    return a + b

import unittest

class TestFunctions(unittest.TestCase):
    def test_iloczyn(self):
        result = iloczyn(2, 3)
        self.assertEqual(result, 6)

    def test_suma(self):
        result = suma(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
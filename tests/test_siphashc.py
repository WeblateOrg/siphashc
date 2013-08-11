import unittest
from siphashc import siphash

class TestSiphashC(unittest.TestCase):
    def test_hash(self):
        result = siphash('sixteencharstrng', 'i need a hash of this')
        self.assertEqual(10796923698683394048L, result)

        result = siphash('0123456789ABCDEF', 'a')
        self.assertEqual(12398370950267227270L, result)

    def test_errors(self):
        with self.assertRaises(ValueError):
            siphash('not long enough', 'a')
        with self.assertRaises(ValueError):
            siphash('toooooooooooooooooooooooo long', 'a')
        with self.assertRaises(ValueError):
            siphash('', 'a')

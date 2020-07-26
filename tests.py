# CS362-SU20, A2-TDD
# Ryan Stachura
# Oregon State University


import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertFalse(check_pwd(""))

    def test2(self):
        self.assertTrue(check_pwd("abcdefghijklmnop"))

    def test3(self):
        self.assertTrue(check_pwd("ABCDEFGHIJKLMNOOP"))

if __name__ == '__main__':
    unittest.main(verbosity=2)

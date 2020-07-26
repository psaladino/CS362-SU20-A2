import unittest
from check_pwd.py import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertFalse(check_pwd(""))

if __name__ == '__main__':
    unittest.main(verbosity=2)

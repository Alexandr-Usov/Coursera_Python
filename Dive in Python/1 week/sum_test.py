"""
It is test for sumnum module
"""

import unittest
import sumnum


class Tests(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sumnum.sum("987"), int(24))


if __name__ == "__main__":
    unittest.main()

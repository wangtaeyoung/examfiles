# -*- coding: utf-8 -*-

import unittest
import tax



class taxTestCase(unittest.TestCase):
    def test_tax(self):
        self.assertEqual(tax.tax(30, 25000,True),int(25000*0.6))


if __name__=="__main__":
    unittest.main(verbosity=2)

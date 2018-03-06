# -*- coding: utf-8 -*-

import unittest
import year



class yearTestCase(unittest.TestCase):
    def test_year(self):
        self.assertEqual(year.isyear(2100),'평년')
        self.assertEqual(year.isyear(1988),'윤년')
        self.assertEqual(year.isyear(1600),'윤년')

    
if __name__=="__main__":
    unittest.main(verbosity=2)

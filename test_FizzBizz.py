# -*- coding: utf-8 -*-

import unittest
import FizzBizz



class FizzBizzTestCase(unittest.TestCase):
    def test_fizzbizz(self):
        self.assertEqual(FizzBizz.fizzbizz(15),'FizzBizz')
        self.assertEqual(FizzBizz.fizzbizz(3),'Fizz')
        self.assertEqual(FizzBizz.fizzbizz(0),'ValueError')


if __name__=="__main__":
    unittest.main(verbosity=2)

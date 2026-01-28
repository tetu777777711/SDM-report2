#!/usr/bin/python3

import unittest
from calc_mul import calc
import sys

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        def test_sample5 (self):
                self.assertEqual (-1, calc(1,999.9))

        def test_sample6 (self):
                self.assertEqual (-1, calc(0,999))

        def test_sample7 (self):
                self.assertEqual (-1, calc(1,1000))

        def test_sample8 (self):
                self.assertEqual (-1, calc(-1111.1,'a'))

        def test_sample9 (self):
                self.assertEqual (-1, calc(None,'a'))

        def test_sample10 (self):
                self.assertEqual (-1, calc(None,-1111.1))

        def test_sample11 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample12 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample13 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample14 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample15 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample16 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample17 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample18 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample19 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample20 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample21 (self):
                x = 10
                self.assertEqual (10, calc(1,x))

        def test_sample22 (self):
                y = sys.float_info.max
                self.assertEqual (-1, calc(10,y))

        def test_sample23 (self):
                y = sys.float_info.max * 1.5
                self.assertEqual (-1, calc(10,y))

        def test_sample24(self):
                y = sys.float_info.min
                self.assertEqual (-1, calc(10,y))

        def test_sample25(self):
                y = sys.float_info.min * 1.5
                self.assertEqual (-1, calc(10,y))

        def test_sample26(self):
                self.assertEqual (21, calc(7,3))

        def test_sample27(self):
                self.assertEqual (-1, calc(10,10.1))

        def test_sample28(self):
                self.assertEqual (-1, calc(10.1,10))

        def test_sample29(self):
                self.assertEqual (-1, calc(10.1,10.1))

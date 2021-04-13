import unittest
from romannum import rom2ar


class RomTest(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(1, rom2ar('I'))

    def test_simple5(self):
        self.assertEqual(5, rom2ar('V'))

    def test_simple10(self):
        self.assertEqual(10, rom2ar('X'))

    def test_simple50(self):
        self.assertEqual(50, rom2ar('L'))

    def test_simple100(self):
        self.assertEqual(100, rom2ar('C'))

    def test_simple500(self):
        self.assertEqual(500, rom2ar('D'))

    def test_simple1000(self):
        self.assertEqual(1000, rom2ar('M'))

    def test_simple3(self):
        self.assertEqual(3, rom2ar('III'))

    def test_simple9(self):
        self.assertEqual(9, rom2ar('IX'))

    def test_simple14(self):
        self.assertEqual(14, rom2ar('XIV'))

    def test_simple990(self):
        self.assertEqual(990, rom2ar('CMXC'))

    def test_compl1776(self):
        self.assertEqual(1776, rom2ar('MDCCLXXVI'))

    def test_compl(self):
        self.assertEqual(1954, rom2ar('MCMLIV'))

    def test_nonst4(self):
        self.assertEqual(4, rom2ar('IIII'))

    def test_nonst499(self):
        self.assertEqual(499, rom2ar('ID'))

    def test_nonst999(self):
        self.assertEqual(999, rom2ar('IM'))

import unittest

from Domains.Number import Number


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.number1 = Number(12,"AB1")
        self.number2 = Number(12,"A2")
        self.number3 = Number(4,"1231")
        self.number4 = Number(4,"21")
        self.digit = Number(12,"5")
        self.digit2 = Number(4,"3")

    def test_addition1(self):
        number1 = Number(16,"54AB6F")
        number2 = Number(16,"CD097D")
        result = number1+number2
        self.assertEqual(result,Number(16,"121B4EC"))

    def test_addition2(self):
        number1 = Number(8,"5677034")
        number2 = Number(8,"1234567")
        result = number1+number2
        self.assertEqual(result,Number(8,"7133623"))

    def test_subtraction1(self):
        number1 = Number(7,"210354")
        number2 = Number(7,"55466")
        result = number1-number2
        self.assertEqual(result,Number(7,"121555"))

    def test_subtraction2(self):
        number1 = Number(2,"100111000")
        number2 = Number(2,"1100111")
        result = number1-number2
        print(result)
        self.assertEqual(result,Number(2,"11010001"))

    def test_multiplication1(self):
        number1 = Number(7,"12345")
        number2 = Number(7,"5")
        result = number1*number2
        self.assertEqual(result,Number(7,"65424"))

    def test_multiplication2(self):
        number1 = Number(16,"A23F4")
        number2 = Number(16,"B")
        result = number1*number2
        self.assertEqual(result,Number(16,"6F8B7C"))

    def test_division1(self):
        number1 = Number(4,"321023")
        number2 = Number(4,"3")
        result = number1//number2
        remainder = number1 % number2
        self.assertEqual(result,Number(4,"103003"))
        self.assertEqual(remainder,Number(4,"2"))

    def test_division2(self):
        number1 = Number(16,"2A0F86")
        number2 = Number(16,"E")
        result = number1//number2
        remainder = number1 % number2
        self.assertEqual(result,Number(16,"3011B"))
        self.assertEqual(remainder,Number(16,"C"))

    def test_conversion_by_substitution1(self):
        number = Number(8,"1735")
        number.base = 10
        self.assertEqual(number,Number(10,"989"))

    def test_conversion_by_substitution2(self):
        number = Number(6,"1054")
        number.base = 16
        self.assertEqual(number,Number(16,"FA"))

    def test_conversion_by_successive_division1(self):
        number = Number(10, "2653")
        number.base = 6
        self.assertEqual(number, Number(6, "20141"))

    def test_conversion_by_successive_division2(self):
        number = Number(16, "BC0D")
        number.base = 6
        self.assertEqual(number, Number(6, "1010513"))

    def test_rapid_conversion1(self):
        number = Number(8, "11024")
        number.base = 2
        print(number)
        self.assertEqual(number, Number(2, "1001000010100"))

    def test_rapid_conversion2(self):
        number = Number(16, "AB650")
        number.base = 8
        print(number)
        self.assertEqual(number, Number(8, "2533120"))

    def test_rapid_conversion3(self):
        number = Number(4, "12131")
        number.base = 16
        print(number)
        self.assertEqual(number, Number(16, "19D"))


if __name__ == '__main__':
    unittest.main()

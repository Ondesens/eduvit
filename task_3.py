import unittest
import sys
def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result
print(factorial(5))
class Test_factorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0),1)
    def test_one(self):
        self.assertEqual(factorial(0),1)
    def test_large_numbers(self):
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(12), 479001600)
    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertEqual(str(context.exception), "Факториал отрицательного числа не определен")
    def test_factorial_positive_numbers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)

if __name__ == '__main__':
    unittest.main()
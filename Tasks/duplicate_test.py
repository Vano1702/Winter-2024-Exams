import unittest
from duplicate import duplicate


class TestSum(unittest.TestCase):
    def test_duplicate(self):
        test_cases = [
            (['abc', 5], ['abc', 'abc', 'abc', 'abc', 'abc']),
            (['abc', 1], ['abc']),
            (['abc', -1], []),
            (['abc', 0], []),
            (['', 0], []),
        ]

        for input_value, expected_output in test_cases:
            with self.subTest(input_value=input_value):
                result = duplicate(input_value[0], input_value[1])
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

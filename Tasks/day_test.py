import unittest
from day import _parse_day


class TestSum(unittest.TestCase):
    def test_parse_day(self):
        test_cases = [
            ('friday', 6),
            ('Friday', -1),
            ('Fri', -1),
            ('monday', 2),
            ('abc', -1),
        ]

        for input_value, expected_output in test_cases:
            with self.subTest(input_value=input_value):
                result = _parse_day(input_value)
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

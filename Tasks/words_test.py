import unittest
from words import words

class TestSum(unittest.TestCase):
    def test_words(self):
        test_cases = [
            ['Hello Marcus Aureluis', 3],
            ['Hello', 1],
            ['', 0],
        ]

        for input_value, expected_output in test_cases:
            with self.subTest(input_value=input_value):
                result = words(input_value)
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

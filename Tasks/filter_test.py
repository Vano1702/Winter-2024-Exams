import unittest
from filter import Filter


class TestSum(unittest.TestCase):
    def test_filter(self):
        test_cases = [
            [[[1, 2, 'three', 4, 5, 'six'], 'int'], [1, 2, 4, 5]],
            [[[-1, 0, 1, 2], 'int'], [-1, 0, 1, 2]],
            [[[-1, 0, 1, 2], 'str'], []],
            [[[True, True, False, 'six'], 'bool'], [True, True, False]],
            [[[], 'str'], []],
        ]

        for input_value, expected_output in test_cases:
            with self.subTest(input_value=input_value):
                result = Filter(input_value[0], input_value[1])
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

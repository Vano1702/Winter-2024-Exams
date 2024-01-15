import unittest
from distinct import distinct


class TestSum(unittest.TestCase):
    def test_distinct(self):
        test_cases = [
            ([1, 2, 1, 3, 1, 4], [1, 2, 3, 4]),
            ([1, 2, -1, 3, 0, 4], [1, 2, -1, 3, 0, 4]),
            ([1], [1]),
            ([1, 1, 1], [1]),
            ([0], [0]),
            ([0, 0], [0]),
            ([0, 0, 0], [0]),
            ([0, 0, 0, 0], [0]),
            ([], []),
            ]

        for input_value, expected_output in test_cases:
            with self.subTest(input_value=input_value):
                result = distinct(input_value)
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

import unittest
from sum import k


class TestSum(unittest.TestCase):
    def test_k(self):
        test_cases = [
            [[5, True, 'string', 7, 'hello'], 12],
            [[5, True, 'string', -7, 'hello'], -2],
            [[0, True, 'string', 0, 'hello'], 0],
            [[1, True, 'string', -1, 'hello'], 0],
            [[5], 5],
            [[-1], -1],
            [[], 0],
        ]

        for input_value, expected_output in test_cases:
            with self.subTest(input_value=input_value):
                result = k(input_value)
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

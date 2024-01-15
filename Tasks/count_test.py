import unittest
from count import count


class TestSum(unittest.TestCase):
    def test_count(self):
        test_cases = [
            ({"a": 1, "b": 'two', "c": 3, "d": 4}, 8),
            ({"a": 1, "b": 'two', "c": -3, "d": 4}, 2),
            ({"a": 0, "b": 'two', "c": 0, "d": -1}, -1),
            ({"a": -1, "b": 'two', "c": -3, "d": -4}, -8),
            ({"a": 1, "b": 'two', "c": -1, "d": 0}, 0),
            ({"a": '1', "b": 'two', "c": 3, "d": 4}, 7),
        ]

        for input_value, expected_output in test_cases:
            with self.subTest(input_value=input_value):
                result = count(input_value)
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

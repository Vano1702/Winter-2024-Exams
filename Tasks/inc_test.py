import unittest
from inc import inc_numbers


class TestSum(unittest.TestCase):
    def test_inc(self):
        test_cases = [
            [
                {"a": 1, "b": 2, "c": 'hello', "d": False},
                {"a": 2, "b": 3, "c": 'hello', "d": False},
            ],
            [
                {"a": 1, "b": 2, "c": 0, "d": -1},
                {"a": 2, "b": 3, "c": 1, "d": 0},
            ],
            [
                {"a": -1, "b": -2},
                {"a": 0, "b": -1},
            ],
            [
                {"a": '-1', "b": '-2'},
                {"a": '-1', "b": '-2'},
            ],
        ]

        for input_value, expected_output in test_cases:
            with self.subTest(input_value=input_value):
                result = inc_numbers(input_value)
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

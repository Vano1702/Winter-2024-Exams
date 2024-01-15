import unittest
from merge import merge_two_objects


class TestSum(unittest.TestCase):
    def test_merge_two_objects(self):
        test_cases = [
            [[{"a": 'uno', "b": 'due'}, {"c": 'tre'}], {"a": 'uno', "b": 'due', "c": 'tre'}],
            [[{"a": 'uno', "b": 'due'}, {"a": 'uno'}], {"a": 'uno', "b": 'due'}],
            [[{"a": 'uno', "b": 'due'}, {"a": 'due'}], {"a": 'due', "b": 'due'}],
            [[{"a": 'uno'}, {"c": 'tre'}], {"a": 'uno', "c": 'tre'}],
            [[{"a": 'uno'}, {}], {"a": 'uno'}],
            [[{}, {}], {}],
        ]

        for input_value, expected_output in test_cases:
            with self.subTest(input_value=input_value):
                result = merge_two_objects(input_value[0], input_value[1])
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

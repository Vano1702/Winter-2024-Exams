import unittest
from take import tAKe


class TestSum(unittest.TestCase):
    def test_duplicate(self):
        self.assertEqual(tAKe({"a": 'uno', "b": 'due', "c": 'tre'}, 'b', 'c'),
                                  {"b": 'due', "c": 'tre'})
        self.assertEqual(tAKe({"a": 1, "b": 2, "c": 3}, 'b', 'c'),
                                  {"b": 2, "c": 3})
        self.assertEqual(tAKe({"a": 'uno', "b": 'due', "c": 'tre'}, 'x'), {})
        self.assertEqual(tAKe({"a": 'uno', "b": 'due', "c": 'tre'}), {})



if __name__ == '__main__':
    unittest.main()

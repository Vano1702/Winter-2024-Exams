import unittest
from take import take


class TestSum(unittest.TestCase):
    def test_duplicate(self):
        self.assertEqual(take({"a": 'uno', "b": 'due', "c": 'tre'}, 'b', 'c'),
                                  {"b": 'due', "c": 'tre'})
        self.assertEqual(take({"a": 1, "b": 2, "c": 3}, 'b', 'c'),
                                  {"b": 2, "c": 3})
        self.assertEqual(take({"a": 'uno', "b": 'due', "c": 'tre'}, 'x'), {})
        self.assertEqual(take({"a": 'uno', "b": 'due', "c": 'tre'}), {})



if __name__ == '__main__':
    unittest.main()

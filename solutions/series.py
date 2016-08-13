import unittest


def slices(string, length):
    if length <= 0:
        raise ValueError('This slice is too short')
    if length > len(string):
        raise ValueError('This slice is very long')
    return [map(int, list(string[i:i + length])) for i in range(len(string) - length + 1)]


class SeriesTest(unittest.TestCase):
    def test_slices_of_one(self):
        self.assertEqual([[0], [1], [2], [3], [4]],
                         slices("01234", 1))

    def test_slices_of_two(self):
        self.assertEqual([[9, 7], [7, 8], [8, 6], [6, 7],
                          [7, 5], [5, 6], [6, 4]],
                         slices("97867564", 2))

    def test_slices_of_three(self):
        self.assertEqual([[9, 7, 8], [7, 8, 6], [8, 6, 7],
                          [6, 7, 5], [7, 5, 6], [5, 6, 4]],
                         slices("97867564", 3))

    def test_slices_of_four(self):
        self.assertEqual([[0, 1, 2, 3], [1, 2, 3, 4]],
                         slices("01234", 4))

    def test_slices_of_five(self):
        self.assertEqual([[0, 1, 2, 3, 4]],
                         slices("01234", 5))

    def test_overly_long_slice(self):
        with self.assertRaises(ValueError):
            slices("012", 4)

    def test_overly_short_slice(self):
        with self.assertRaises(ValueError):
            slices("01234", 0)


if __name__ == '__main__':
    unittest.main()
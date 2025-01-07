"""Module to unittest algorithms"""

import unittest
from unittest.mock import Mock

import src.algorithms as algorithms


class TestMain(unittest.TestCase):

    def test_bubble_sort(self):
        """Bubble sort: test correct sorting"""
        draw_data_mock = Mock()

        data = [9, 2, 7, 5, -1, 5, 23, 0, 61, 8, 9, 11, -22]

        algorithms.bubble_sort_algorithm(data, draw_data_mock, 0)

        self.assertEqual([-22, -1, 0, 2, 5, 5, 7, 8, 9, 9, 11, 23, 61], data)

    def test_quick_sort(self):
        """Quick sort: test correct sorting"""
        draw_data_mock = Mock()

        data = [9, 2, 7, 5, -1, 5, 23, 0, 61, 8, 9, 11, -22]

        algorithms.quick_sort_algorithm(data, draw_data_mock, 0, len(data) - 1, 0)

        self.assertEqual([-22, -1, 0, 2, 5, 5, 7, 8, 9, 9, 11, 23, 61], data)

    def test_merge_sort(self):
        """Merge sort: test correct sorting"""

        draw_data_mock = Mock()

        data = [9, 2, 7, 5, -1, 5, 23, 0, 61, 8, 9, 11, -22]

        algorithms.merge_sort_algorithm(data, draw_data_mock, 0, len(data) - 1, 0)

        self.assertEqual([-22, -1, 0, 2, 5, 5, 7, 8, 9, 9, 11, 23, 61], data)


if __name__ == '__main__':
    unittest.main()

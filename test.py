import unittest

import numpy as np

from radialphonic import poly_centroid, poly_intersect


class TestRadialphonic(unittest.TestCase):
    def setUp(self):
        self.square = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.eqtri = [[0, 0], [1, 0], [1/2, np.sqrt(3)/2]]

    def test_poly_centroid(self):
        cx, cy = poly_centroid(self.square)
        self.assertAlmostEqual(cx, 0.5, 7, 'wrong x-centroid for a square')
        self.assertAlmostEqual(cy, 0.5, 7, 'wrong y-centroid for a square')

        cx, cy = poly_centroid(self.eqtri)
        self.assertAlmostEqual(cx, 0.5, 7,
                               'wrong x-centroid for an equilateral triangle')
        self.assertAlmostEqual(cy, np.sqrt(3)/6, 7,
                               'wrong y-centroid for an equilateral triangle')

    def test_poly_intersect(self):
        ix, iy = poly_intersect((0, 0), (0, 2), (-1, 1), (1, 1))
        self.assertAlmostEqual(ix, 0, 7,
                               'wrong x-intersection point for cross')
        self.assertAlmostEqual(iy, 1, 7,
                               'wrong y-intersection point for cross')

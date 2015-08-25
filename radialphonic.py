"""
Inspired from: http://1ucasvb.tumblr.com/post/42881722643/the-familiar-trigonometric-functions-can-be

Given an arbitrary polygon, first identify the bottom and top boundaries and set
those to -/+ range with midpoint equal to zero. Next, find the centroid of the
polygon and sweep a ray from the center to the edge, producing a sample value.
Determine one period of the shape, then convert that into an audio tone.

Note, the reverse should also be doable - i.e. given a single period of a pure
tone, create the polygon that represents it

e.g.
 A circle will produce a sin wave
 Regular polygons will create tones approaching a pure sin wave as the number
 of sides increases. What about irregular concave or convex polygons?
"""
import matplotlib.pyplot as plt
import numpy as np


def poly_intersect(a1, a2, b1, b2):
    x = (((a1[0]*a2[1] - a1[1]*a2[0])*(b1[0] - b1[0]) -
         (a1[0] - a2[0])*(b1[0]*b2[1] - b1[1]*b2[0])) /
         ((a1[0] - a2[0])*(b1[1] - b2[1]) - (a1[1] - a2[1])*(b1[0] - b2[0])))
    y = (((a1[0]*a2[1] - a1[1]*a2[0])*(b1[1] - b1[1]) -
         (a1[1] - a2[1])*(b1[0]*b2[1] - b1[1]*b2[0])) /
         ((a1[0] - a2[0])*(b1[1] - b2[1]) - (a1[1] - a2[1])*(b1[0] - b2[0])))
    return x, y


def poly_centroid(points):
    _points = np.vstack((points, points[0]))
    x, y, area = 0, 0, 0
    for p1, p2 in zip(_points[:-1], _points[1:]):
        c = p1[0]*p2[1] - p2[0]*p1[1]
        area += c
        x += (p1[0] + p2[0]) * c
        y += (p1[1] + p2[1]) * c
    return x / (3*area), y / (3*area)


if __name__ == '__main__':
    polygon = [[0, 0], [1, 0], [1, 1], [0, 1]]
    centroid = poly_centroid(polygon)
    print(centroid)
    fs = 100
    angles = np.linspace(0, 2*np.pi, fs)


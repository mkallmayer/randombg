#!/usr/bin/python3
from PIL import Image as image
import numpy as np
from random import randrange as rr
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import scipy.misc

WIDTH = 300
HEIGHT = 300
EPSILON = 0.001

# select a few random pixels as spots
spots = np.array([[rr(0,WIDTH), rr(0, HEIGHT)] for i in range(0,rr(3,6))], dtype=np.float64)
# assign random rgb values to spots
spot_cols = np.array([[rr(0,255) for i in range(3)] for j in range(len(spots))], dtype=np.float64)

def metric1(xpos, ypos):
    return abs(xpos[0] - ypos[0]) + abs(xpos[1] - ypos[1])

def metric2(xpos, ypos):
    return np.sqrt((xpos[0] - ypos[0])**2 + (xpos[1] - ypos[1])**2)

grid = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)

for y in range(HEIGHT):
    for x in range(WIDTH):
        dists = np.zeros((len(spots)), dtype=np.uint8)
        for s in range(len(spots)):
            dists[s] = metric1(spots[s], [x, y])
        index = np.argmin(dists)
        grid[x, y] = spot_cols[index]

grid = grid
im = image.fromarray(grid)
im.save("out.png")

#!/usr/bin/python3
from PIL import Image as image
import numpy as np
from random import randrange as rr

# this has horrible performance

WIDTH = 800
HEIGHT = 800

# select a few random pixels as spots
spots = np.array([[rr(0,WIDTH), rr(0, HEIGHT)] for i in range(0,rr(5,10))], dtype=np.float64)
# assign random rgb values to spots
spot_cols = np.array([[rr(0,255) for i in range(3)] for j in range(len(spots))], dtype=np.float64)

def metric(xpos, ypos):
    return abs(xpos[0] - ypos[0]) + abs(xpos[1] - ypos[1])

grid = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)

for y in range(HEIGHT):
    for x in range(WIDTH):
        dists = np.zeros((len(spots)), dtype=np.uint8)
        for s in range(len(spots)):
            dists[s] = np.linalg.norm(spots[s] - [x, y])
        totaldists = dists.sum()
        for s in range(len(spots)):
            grid[x, y] += (spot_cols[s] * (dists[s]/totaldists)).astype(np.uint8)

grid = grid
im = image.fromarray(grid)
im.save("out.png")

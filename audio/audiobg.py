#!/usr/bin/python3

import pyaudio
import numpy as np
from PIL import Image as image
from sys import argv as argv

if (len(argv) <2):
    print("audiobg.py: Creates a background image from microphone noise \n Usage: audiobg.py <filename.png>")
    exit()

CHUNK = 1200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SAMPLES = 4

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = np.zeros((SAMPLES*CHUNK), dtype=np.uint8)

for i in range(0, int(SAMPLES)):
    data = stream.read(CHUNK)
    frames[i*CHUNK:(i+1)*CHUNK] = np.frombuffer(data, dtype=np.uint8)[0:1200]

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

img1 = np.tile(frames[0:2400].reshape(800, 3), (800, 1, 1))
img2 = np.tile(frames[2400:4800].reshape(800, 3), (800, 1, 1)).transpose([1,0,2])
img = (img1 + img2) >> 1
im = image.fromarray(img)
im.save("{}".format(argv[1]))

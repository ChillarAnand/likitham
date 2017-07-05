"""
Generates training data using chamanti OCR
"""

import os
import sys

from PIL import Image as im

import telugu
from scribe import Scribe


def bin_arr_to_rgb_img(arr):
    return bin_arr_to_img(arr).convert("RGB")


def bin_arr_to_img(arr):
    return im.fromarray((255 * (1 - arr)).astype("uint8"))


options = {
    'size': 24,
    'maxangle': 0,
    'dtype': 'float32',
    'vbuffer': 0,
    'noise': 0.05,
    'hbuffer': 5,
    'nchars_per_sample': 1,
    'height': 45
}
alphabet_size = len(telugu.symbols)

scriber = Scribe(language=telugu, **options)

if len(sys.argv) > 1:
    target_dir = sys.argv[1]
    samples = int(sys.argv[2])
else:
    samples = 100
    target_dir = 'data'

print(samples, target_dir)

try:
    os.makedirs(target_dir)
except FileExistsError:
    pass

for i in range(samples):
    image, text, labels = scriber.get_text_image()
    image = bin_arr_to_img(image)

    base_name = '{}/{:04d}'.format(target_dir, i)
    image.save(base_name + '.png')

    with open(base_name + '.gt.txt', 'w') as fh:
        fh.write(''.join(text))

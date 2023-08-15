import os
from ..core import imager

def test_blank_image_generation():
    img = imager.generateBlankImage(300, 200)

    assert img.shape == (300, 200, 3)

    for x in range(300):
        for y in range(200):
            assert list(img[x, y]) == [255, 255, 255]

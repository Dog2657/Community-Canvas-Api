import numpy as np
import cv2

def save(path: str, img: np.ndarray):
    cv2.imwrite(path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])


def generateBlankImage(width: int, height: int) -> np.ndarray:
    img = np.ones((height, width, 3))
    img = img * 255
    return img


def updatePixel(path: str, x: int, y: int, rgb: tuple):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    img = img[:,:,:3]

    img[x, y] = [rgb[2], rgb[1], rgb[0]]

    return img
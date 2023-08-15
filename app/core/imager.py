import numpy as np
import cv2

def save(path: str, img: np.ndarray):
    cv2.imwrite(path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

def generateBlankImage(width: int, height: int) -> np.ndarray:
    img = np.ones((width, height, 3))
    img = img * 255
    return img


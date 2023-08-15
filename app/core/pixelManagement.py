from core import imager
import config
import math
import os

def getSectionDetailsFromXY(x: int, y: int):
    section_width = math.floor(config.Canvas_Width / config.Canvas_Colums)
    section_heigth = math.floor(config.Canvas_Height / config.Canvas_Rows)

    horizontalSections = math.floor(x / section_width)
    verticalSections = math.floor(y / section_heigth)

    sectionIndex = horizontalSections + (verticalSections * config.Canvas_Colums)

    X = x - (horizontalSections * section_width)
    Y = y - (verticalSections * section_heigth)

    return sectionIndex, X, Y


def updateCanavasPixel(x: int, y: int, rgb: tuple):
    sectionIndex, X, Y = getSectionDetailsFromXY(x, y)

    path = f'{os.getcwd()}/sections/{sectionIndex}.png'

    img = imager.updatePixel(path, X, Y, rgb)

    imager.save(path, img)

    print(path)
    
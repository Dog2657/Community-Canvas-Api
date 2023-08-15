from ..core import imager
import shutil
import os

def test_image_generation():
    img = imager.generateBlankImage(300, 200)

    assert img.shape == (200, 300, 3)

    for x in range(300):
        for y in range(200):
            assert list(img[y, x]) == [255, 255, 255]


def test_image_saving():
    os.makedirs(f'{os.getcwd()}/app/.temp/', exist_ok=True)
    path = f'{os.getcwd()}/app/.temp/image.png'

    img = imager.generateBlankImage(300, 200)
    imager.save(path, img)

    assert os.path.exists(path)

    shutil.rmtree('/'.join(path.split('/')[0:-1]))



def test_pixel_update_0_0():
    os.makedirs(f'{os.getcwd()}/app/.temp/', exist_ok=True)
    path = f'{os.getcwd()}/app/.temp/image.png'

    img = imager.generateBlankImage(500, 500)
    imager.save(path, img)

    X = 0
    Y = 0
    rgb = (0, 0, 0)

    imgArray = imager.updatePixel(path, X, Y, rgb)

    assert len(img) == len(imgArray)
    assert imgArray.shape == (500, 500, 3)

    for x in range(len(imgArray)):
        for y in range(len(imgArray[x])):
            if(x == X and y == Y):
                assert (imgArray[x, y] == rgb).all()

            else:
                assert (img[x, y] == imgArray[x, y]).all()

    shutil.rmtree('/'.join(path.split('/')[0:-1]), onerror=None)
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

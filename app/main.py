from fastapi import FastAPI
from core import imager
import config
import math
import os

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    if not os.path.isdir('sections'):
        os.makedirs("sections")

    section_width = math.floor(config.Canvas_Width / config.Canvas_Colums)
    section_heigth = math.floor(config.Canvas_Height / config.Canvas_Rows)

    for index in range(
        config.Canvas_Colums * config.Canvas_Rows
    ):
        path = f'{os.getcwd()}/sections/{index}.png'

        if not os.path.isfile(path):
            img = imager.generateBlankImage(section_width, section_heigth)
            imager.save(path, img)


@app.get("/config")
async def GET_Canvas_Config():
    ...


@app.post("/update")
async def POST_Update_Pixel():
    ...


@app.websocket("/wsnotifier")
async def WEBSOCKET_Notifier():
    ...
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, HTTPException, BackgroundTasks
from core import imager, notifierManager, validation, pixelManagement
from fastapi.staticfiles import StaticFiles
import config
import math
import os

app = FastAPI()
wsmanager = notifierManager.Manager()

app.mount("/sections", StaticFiles(directory="sections"), name="sections")


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
    return {
        "width": config.Canvas_Width,
        "height": config.Canvas_Height,
        "colums": config.Canvas_Colums,
        "rows": config.Canvas_Rows,
        "minDisplay": {
            "width": config.Canvas_Min_Width,
            "height": config.Canvas_Min_Height
        }
    }


@app.post("/update")
async def POST_Update_Pixel(
    background_tasks: BackgroundTasks,
    request: Request,
    x: int,
    y: int,
    red: int,
    green: int,
    blue: int
):
    if(not validation.isOnCanvas(x, y)):
        raise HTTPException(status_code=400, detail="Invalid X/Y position")
   
    if(not validation.isValidRGB(red, green, blue)):
        raise HTTPException(status_code=400, detail="Invalid rgb value")
    
    background_tasks.add_task(pixelManagement.updateCanavasPixel, x, y, (red, green, blue))
    await wsmanager.alertOfUpdate(x, y, (red, green, blue))



@app.websocket("/wsnotifier")
async def WEBSOCKET_Notifier(websocket: WebSocket):
    await wsmanager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    
    except WebSocketDisconnect:
        wsmanager.disconnect(websocket)
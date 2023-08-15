from fastapi import FastAPI


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    ...


@app.get("/config")
async def GET_Canvas_Config():
    ...


@app.post("/update")
async def POST_Update_Pixel():
    ...


@app.websocket("/wsnotifier")
async def WEBSOCKET_Notifier():
    ...
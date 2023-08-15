from fastapi import WebSocket

class Manager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def alertOfUpdate(self, x: int, y: int, rgb: tuple):
        for connection in self.active_connections:
            await connection.send_json({
                "location": {
                    "x": x,
                    "y": y
                },
                "value": {
                    "r": rgb[0],
                    "g": rgb[1],
                    "b": rgb[2]
                }
            })
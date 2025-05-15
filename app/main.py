from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
from auth import get_current_user
from chat_ws import ConnectionManager

app = FastAPI()
manager = ConnectionManager()


@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket, user: str = Depends(get_current_user)):
    await manager.connect(websocket, user)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{user}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{user} left the chat")

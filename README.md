# 💬 Real-Time Chat App using FastAPI + WebSockets

A minimal real-time chat system using FastAPI WebSocket support and simple bearer token auth.

## Features
- WebSocket-based real-time communication
- Basic bearer token-based user simulation
- Broadcast messages to all connected users
- Easy to extend with real auth + Redis pub/sub

## Run Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Start FastAPI server

    uvicorn app.main:app --reload
3. Use a WebSocket client (e.g. browser, Postman)
    Connect to: ws://localhost:8000/ws/chat

    Header: Authorization: Bearer mysecrettoken

    Send/receive chat messages in real-time
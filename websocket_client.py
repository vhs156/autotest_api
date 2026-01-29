import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Hello World"
        print(f"Sending message: {message}")
        await websocket.send(message)
        #
        # response = await websocket.recv()
        # print(f"Received message: {response}")

        for _ in range(5):
            response = await websocket.recv()
            print(f"Received message: {response}")

asyncio.run(client())

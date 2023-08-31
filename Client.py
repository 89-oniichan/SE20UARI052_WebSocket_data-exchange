import asyncio
import websockets

async def communicate():
    uri = "ws://ipaddrr:portNO/api/messages"
    
    async with websockets.connect(uri) as websocket:
        async def send():
            while True:
                message = input("Enter message to send to server: ")
                await websocket.send(message)
                print("Message sent to server")

        async def receive():
            while True:
                response = await websocket.recv()
                print(f"Received message from server: {response}")

        await asyncio.gather(send(), receive())

asyncio.get_event_loop().run_until_complete(communicate())


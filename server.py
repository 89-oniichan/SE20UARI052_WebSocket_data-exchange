import asyncio
import websockets

async def receive_message(websocket, path):
    async for message in websocket:
        print(f"Received message from client: {message}")
        
        response = input("Enter response to send to client: ")
        await websocket.send(response)
        print("Response sent to client")

start_server = websockets.serve(receive_message, "0.0.0.0", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

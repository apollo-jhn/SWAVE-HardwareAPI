import asyncio
from websockets.asyncio.server import serve

async def handler(websocket):
  while True:
    try:
      message = await websocket.recv()
    except:
      break
    print(message)

async def main():
  async with serve(handler, "", 8001) as server:
      await server.serve_forever()

def init():
  asyncio.run(main())
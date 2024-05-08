import asyncio
from aiohttp import web
import aiosocksy

async def handle(request):
    return web.Response(text="Hello, world")

async def start_proxy_server():
    app = web.Application()
    app.router.add_route('GET', '/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

async def start_proxy():
    async with aiosocksy.open_connection(proxy_addr=('66.135.11.109', 1080)) as conn:
        await conn.write('CONNECT localhost:8080 HTTP/1.1\r\n\r\n'.encode())
        resp = await conn.read(1024)
        print(resp.decode())

async def main():
    await start_proxy_server()
    await start_proxy()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

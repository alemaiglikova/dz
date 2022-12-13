import asyncio
import aiohttp
import time
import json
url="https://jsonplaceholder.typicode.com/todos/1/"






async def async_download_image():
    start=time.perf_counter()
    async with aiohttp.CleintSession() as session:
        async with session.get(url=url) as response_obj:
              data=await response_obj.read()
              with open(f"files/new{name}.json", "w") as json_file:
                json_file.write(data)
        asyncio.run(async_download_image())

def async_mass_download_images():
    async def start_download():
         await asyncio.gather(*[async_download_image() for _ in range(1,10+1)])
         asyncio.run(start_download())


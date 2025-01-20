
'''
what is multiprocessing?
- multiprocessing is a package that supports spawning processes using an API similar to the threading module.
- multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.
- The multiprocessing module also introduces APIs which do not have analogs in the threading module.
- multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.
'''
import multiprocessing
import aiohttp
import asyncio

async def download_image(i):
    url = "https://4kwallpapers.com/images/wallpapers/bugatti-bolide-3840x2160-20441.jpg"
    filename = f"image_{i}.jpg"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(filename, "wb") as file:
                file.write(data)
            print(f"Image downloaded {filename}")

async def main():
    tasks = [download_image(i) for i in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(main())
     

import aiohttp
import asyncio

def write_image(data, filename):
    with open(filename, "wb") as file:
        file.write(data)
    print(f"Image downloaded {filename}")

async def async_function_one():
    url = "https://4kwallpapers.com/images/wallpapers/bugatti-bolide-3840x2160-20441.jpg"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            write_image(await response.read(), "14_async_multithreading/image1.jpg")

async def async_function_two():
    url = "https://4kwallpapers.com/images/wallpapers/bugatti-bolide-3840x2160-20441.jpg"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            write_image(await response.read(), "14_async_multithreading/image2.jpg")

async def async_function_three():
    url = "https://4kwallpapers.com/images/wallpapers/bugatti-bolide-3840x2160-20441.jpg"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            write_image(await response.read(), "14_async_multithreading/image3.jpg")

async def main():
    await asyncio.gather(
        async_function_one(),
        async_function_two(),
        async_function_three()
    )

asyncio.run(main())

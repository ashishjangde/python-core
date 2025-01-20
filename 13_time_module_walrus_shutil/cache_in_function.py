import functools;

@functools.lru_cache()
def get_data():
    import requests
    data = requests.get("https://jsonplaceholder.typicode.com/posts")
    return data.json()

print(get_data())
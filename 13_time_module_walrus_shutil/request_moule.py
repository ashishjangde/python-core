import requests

# data = requests.get("https://jsonplaceholder.typicode.com/posts")

# for d in data.json():
#     print(d['title'])

data2 = requests.post("https://jsonplaceholder.typicode.com/posts", 
    data={
        'title': 'ashish',
        'body': 'jangde',
        'userId': 100
    })

print(data2.json())

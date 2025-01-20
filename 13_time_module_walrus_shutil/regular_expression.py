import re

string = '''
This is a story about a young programmer named Alex who loved coding in Python. One day,
while debugging a particularly tricky function, Alex discovered a hidden pattern in the code.
The pattern revealed itself like a puzzle waiting to be solved. With determination and countless cups of coffee,
Alex worked through the night. By morning, not only had the bug been fixed, but the entire system was running more
efficiently than ever before. The team was amazed at how a single night's work could transform their project.
'''
result = re.findall(r'\b[Aa]\w+', string)  # \b is a word boundary  # \w is a word character + is one or more

print(result)
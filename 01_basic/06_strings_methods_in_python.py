a = "!!!!ashish jangde!!!!"
print(a)
print(a.strip("!")) # ashish jangde
print(a.lstrip("!")) # ashish jangde!!!!
print(a.rstrip("!")) # !!!!ashish jangde
print(a.replace("!", "")) # ashish jangde
print(a.count("!")) # 8
print(a.find("a")) # 4
print(a.find("z")) # -1
print(a.upper()) # !!!!ASHISH JANGDE!!!!
print(a.lower()) # !!!!ashish jangde!!!!
print(a.title()) # !!!!Ashish Jangde!!!!
b = "ashish"
print(b.capitalize()) # Ashish
print(a.isprintable()) # True
print(a.isalpha()) # False with spaces and special characters
print(b.isalpha()) # True
print(a.isdigit()) # False
print(b.isdigit()) # False
c = "123"
print(c.isdigit()) # True
print(a.isalnum()) # False with spaces and special characters
print(a.swapcase()) # !!!!!ASHISH JANGDE!!!!
print(a.startswith("!")) # True
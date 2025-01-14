f = open("11_file_handeling/ashish.txt", "r")  # This will open the file in append mode

while True:
     line = f.readline()
     print(line)
     if not line:
         break
     
f.close()


c = open("11_file_handeling/ashish.txt", "a")  # This will open the file in append mode

l = ["\nThis is the first line\n", "This is the second line\n", "This is the third line\n"]
c.writelines(l)

c.close()
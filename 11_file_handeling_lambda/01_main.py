# material = open("11_file_handeling/file.txt", "r")

# lead =material.read()  # This will read the file and return the content of the file as a string

# print(lead)
# material.close()  # This will close the file  it is important to close the file after reading or writing to it to free up the resources

f = open("11_file_handeling/ashish.txt", "a")  # This will open the file in append mode

f.write("\nHello from ashish.txt")
f.close()
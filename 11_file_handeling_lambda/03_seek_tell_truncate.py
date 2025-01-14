
# Now open in read mode to demonstrate seek and tell
with open("11_file_handeling/ashish.txt", "r") as f:
    # tell() shows current position
    print(f"Current position: {f.tell()}")
    
    # read first 5 characters
    print(f.read(5))
    print(f"After reading 5 chars, position: {f.tell()}")
    
    # seek(0) moves cursor to start
    f.seek(0)
    print(f"After seek(0), position: {f.tell()}")
    
    # read everything
    print(f.read())

# Demonstrate truncate
with open("11_file_handeling/file2.txt", "w") as f:
    f.write("This is a long text that will be truncated")
    # truncate file to 10 characters
    f.truncate(10)
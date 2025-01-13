import os
import shutil

os.chdir("09_os_module")

for i in range(5):
    dir_name = f"dir_{i+1}"
    file_path = os.path.join(dir_name, "main.py")

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"{dir_name} created")

        # Create and open the file using 'with open' for safety
        with open(file_path, "w") as file:  # 'w' is for write mode and 'r' is for read mode with open means open the file in read mode
            print(f"main.py created in {dir_name}")
            
            # Write to the file
            file.write("def print_hello():\n   print(\"Hello from print_statement.py\")\n\nprint_hello()")
            
    else:
        shutil.rmtree(dir_name)
        print(f"{dir_name} deleted")

print(os.getcwd())

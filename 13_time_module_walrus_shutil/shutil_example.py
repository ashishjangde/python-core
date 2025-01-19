import shutil
import os

os.chdir("13_time_module_walrus_shutil")

if os.path.exists('example.txt'):
	# shutil.copy('example.txt', 'example_copy.txt')
 	shutil.copy2('example.txt', 'example_copy.txt') # copy2() also copies the metadata of the file
else:
	print("Source file 'example.txt' does not exist")
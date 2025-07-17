import os

# //Specify the directory 
directory_path = 'D:\python'

# get directory list 
contents = os.listdir(directory_path)

# Iterate each item 
for item in contents:
    print(item)

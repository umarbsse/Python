# f  = open("F:/Python/Chapter 9/write_file.txt") # if file not found get base path like full path
# print(f.read())
# f.close()



# Same can be be done without closing the file no need to mention the files status

with open("F:/Python/Chapter 9/write_file.txt") as f:
    print(f.read())


#####
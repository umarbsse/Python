f  = open("F:/Python/Chapter 9/multiple_lines_file.txt") # if file not found get base path like full path

#lines = f.readlines()

#print(lines, type(lines))


single_line = f.readline()
print(single_line)
single_line = f.readline()
print(single_line)
single_line = f.readline()
print(single_line)
single_line = f.readline()
print(single_line)
single_line = f.readline()
print(single_line)

f.close()
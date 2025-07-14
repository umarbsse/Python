name= "Umer Shahzad"
startwith = name[0]
Firstnam = name[0:4]
lastnam = name[5:12]
print(startwith)
print(Firstnam)
print(lastnam)

# Slicing string with negaive indexs   

Firstnam = name[-12:-8]
lastnam = name[-7:]
print(Firstnam)
print(lastnam)

# Slicing string like left or right


Firstnam = name[:-8]
lastnam = name[-7:]
print(Firstnam)
print(lastnam)


#String slicing with skip values

str= "Pakistan"
sliced = str[0:6]
skip_sliced = str[0:5:2]
print(str)
print(sliced)
print(skip_sliced)
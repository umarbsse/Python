a = (1,456,True, "Umer", "Essa")
print(a)
#a[2] = "Ali" # Touple can not be changed its throws error
#print(a)
count = a.count(1) # return the occurance of the element in the tuple
print(count)

index = a.index(120)  #return index of element if exsit and error if not exist 

print(index)

is_element_exist = 1 in a
print(is_element_exist)
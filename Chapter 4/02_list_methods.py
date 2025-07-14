list = ["umer","ali",32,False,1.34]
print(list)
print(list[1])
list[1] = 'Essa'
print(list)
print(list[1])
print(list[1:3]) #slicing works as it works on the string
print(list[0:4:2]) #slicing works as it works on the string


list_1 = [56,34,6789,4345,2,123,0,1]
list_1.sort() # Sort ascendin order
print(list_1) 
list_1.reverse() # Sort descing order
print(list_1)

list_1.insert(1,222) #insert at index 1 and moved the alread inserted elemnt at index 1 to next index
print(list_1)
list_1.append(33333) # insert at end of list
print(list_1)

list_1.pop(4) # remove element at index 4
print(list_1)


value = list_1.pop(1)
print(value)
print(list_1)


list_1.remove(33333)  #remove element from list by value
print(list_1)
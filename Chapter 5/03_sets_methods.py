set_1 = {1,2,3}

set_1.add(67) # add elements in set
print(set_1)


print(len(set_1)) # get length of set

set_1.remove(2)  # remove the elemnt from set

set_1.pop() # remove the random elemnt from set

#set_1.clear()    #empty the set


print(set_1)



set_2 = {12,123,456,456,1,2,3}


print(set_1.union(set_2))


print(set_1.intersection(set_2))

print(set_1.issubset(set_2))

print(set_2.issubset(set_1))

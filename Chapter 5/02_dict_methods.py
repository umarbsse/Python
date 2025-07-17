marks = {
    "Umer":100,
    "Essa":78,
    "Ali":99,
    'class':[1,2,3,4,5,6,6,7]
}
# print(marks.items())    #Key value pair
# print(marks.keys())     #Keys
# print(marks.values())   #Values

marks.update( {"Umer":99, 'class':[1,2,3] , 'section':['A','B','C']})   #Update key value pair because its updateable

#print(marks)

print(marks.get("Umer2")) # Prints None if key not exist
print(marks["Umer2"]) # return Error if key not exist
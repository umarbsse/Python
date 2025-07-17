marks1= int(input("Enter Marks 1: "))
marks2= int(input("Enter Marks 2: "))
marks3= int(input("Enter Marks 3: "))
average= ((marks1+marks2+marks3)/300)*100
if(average>=40):
    print("you passed ", average)
else:
    print("You failed, try again next year", average)
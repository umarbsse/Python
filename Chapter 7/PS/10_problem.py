'''
print table in reverse order
'''
n = int(input("Enter the number: "))
#for i in range(1,11):
#    print(f"{n} x {11-i} = {n*(11-i)}")


for i in range(10,0,-1):
    print(f"{n} x {i} = {n*(i)}")
'''
for n =3
*
***
*****
'''
n = int(input("Enter the number: "))
for i in range (1, n+1):
    print("*"*i,end="")   # end="" used for not printing new line
    print()
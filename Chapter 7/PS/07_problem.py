'''
for n =3
  *
 ***
*****
for n = 9
        *
       ***
      *****
     *******
    *********
   ***********
  *************
 ***************
*****************
'''
n = int(input("Enter the number: "))
for i in range (1, n+1):
    print(" "* (n-i),end="")   # end="" used for not printing new line
    print("*"* (2*i-1),end="")
    print()
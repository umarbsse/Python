'''
   factorial (0) =  1
   factorial (1) =  1
   factorial (2) =  2*1
   factorial (3) =  3*2*1
   factorial (4) =  4*3*2*1
   factorial (5) =  5*4*3*2*1
   factorial (n) =  n* factorial(n-1)
'''

# recursion is slef calling function....
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
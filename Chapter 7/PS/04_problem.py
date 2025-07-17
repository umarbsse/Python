n = int (input("Enter a number: "))
for i in range(2,n):
    if(n%i)==0:
        print(f"Number {i} is not prime")
        break
else:
    print(f"Number {n} is prime")

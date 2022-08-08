n = int(input("Enter a number:"))
n = int(n)
sum=0
for i in range(2,n+1):
    for q in range(2,i):
        if(i%q==0):
            break
        
    else:
        print(i, "Is a prime number")
        sum = sum+i

print("sum of prime numbers is", sum)
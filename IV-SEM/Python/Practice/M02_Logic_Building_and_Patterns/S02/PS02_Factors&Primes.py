'''
Print all thr factors of a given numbers
input : 12
output : 1 2 3 4 6 12
'''
'''
n = int(input("Enter a number : "))
for i in range(1, n+1):
    if n % i == 0:
        print(i,end=" ")
'''
'''
count the numbers of factors of a given number
input : 12
output : 6
'''
'''
n = int(input("Enter a number : "))
count = 0 
for i in range(1, n+1):
    if n % i == 0:
        count += 1
print(count)
'''
'''
Check whether a given number is prime or not
input : 7
output : prime

input : 9
output : not prime
'''
n = int(input("Enter a number : "))
if n < 2:
    print("not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("not prime")
            break
    else:
        print("prime")

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
'''
'''
n = int(input("Enter a number : "))
counter = 0
for i in range(2, n//2+1):
    if n % i == 0:
        counter += 1
if counter == 0 and n > 1:
    print("prime")
else:
    print("not prime")
'''
'''
print all the prime numbers in the given range
input : 1 10
output : 2 3 5 7
'''
'''
a, b = map(int, input("Enter the range : ").split())
for num in range(a, b+1):   
    if num > 1:  
        for i in range(2, num):  
            if (num % i) == 0:  
                break  
        else:  
            print(num, end=" ")
'''
# read a number from cthe user and print its factorial
''' 
n = int(input("Enter a number : "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)
'''
'''
# GCD
intput : 12 and 24
output : 12
'''
'''
a, b = map(int, input("Enter two numbers : ").split())
while b:
    a, b = b, a % b
print(a)
'''

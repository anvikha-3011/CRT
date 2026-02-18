'''
1. Square Star Pattern
n = 4

n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
'''
'''
2. Right Angle Triangle Pattern
n = 4

n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

'''
'''
3. Inverted Triangle Pattern
n = 4

n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
'''
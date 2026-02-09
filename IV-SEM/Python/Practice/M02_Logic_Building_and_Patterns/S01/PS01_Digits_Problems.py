'''
sample input : 1234
sample output : 4

sample input : 12236
sample output : 5
'''
'''
n = int(input("Enter a number: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print(count)
'''
'''
sample input : 1234
sample output : 10

sample input : 12236
sample output : 14
'''
'''
n = int(input("Enter a number: "))
sum_of_digits = 0
while n > 0:
    digit = n % 10
    sum_of_digits += digit
    n = n // 10
print(sum_of_digits)    
'''
'''
sample input : 1234
sample output : 24

sample input : 12236
sample output : 226
'''
'''
n = int(input())
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        print(digit,end=" ")
    n = n // 10
'''
'''
sample oinput : 1234
sample output : 4321
'''
'''
n = int(input())
num = 0
while n > 0:
    digit = n % 10
    num = num * 10 + digit
    n = n // 10
print(num)
'''

'''
sample input : 12256
sample output : 2 2 6
'''
'''
n = int(input())
palindrome = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if palindrome == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
'''
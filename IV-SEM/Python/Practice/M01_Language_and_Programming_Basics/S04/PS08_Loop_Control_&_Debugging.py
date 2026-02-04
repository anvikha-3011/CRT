'''
Finding and Fixing of Errors called Debugging
Types of Errors:
1. Syntax Errors --> Missing of Colon, Missing of indentation
2. Runtime Errors --> Any num is divisble by Zero
3. Logical Errors --> Missing of Logics
Debugging Techniques:
1. Print()
2. try-except
3. Using pdb
'''
'''
a = int(input("Enter a number: "))
b = int(input("Enter another number"))
c = a+b
print("value of a :", a)
print("value of b :", b)
print("Sum of a and b is :", c)

'''
'''
try: 
    a = int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("can not divisible by Zero")
except ValueError:
    print("Invalid input.")
'''
import pdb

def add(a,b):
    pdb.set_trace()
    return a+b
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(add(a,b))

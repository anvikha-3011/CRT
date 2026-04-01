'''
#1) Find the Largest Number (Using max())
#input : [12,78,32,54,69,100]
#output : 100

#Code:
li = [12,78,32,54,69,100]
max_num = li[0]
for ele in li:
    if ele > max_num:
        max_num = ele
print(max_num)
'''
'''
#2) Check palindrome (Using reversed() & join())
s = input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

#Using join and reversed()
s = input()
if s == ''.join(reversed(s)):
    print("Palindrome")
else:
    print("Not a Palindrome")

#Count even numbersusing filter()
li = [1,2,3,4,5]
res = list(filter(lambda x: x%2==0, li))
print(len(res))

#Remove duplicates from a list using set()
li = [1,2,3,4,5,1,2]
print(set(li))

#Sum of digit using sum()
n = int(input())
res = sum(int(digit) for digit in str(n))
print(res)

#Sort words alphabetically using sorted()
wordds = ["banana", "apple", "grape", "orange"]
sorted_words = sorted(wordds)
print(sorted_words) 
'''
#Find Second Largest Number
li = [10,20,30,40,50,60,70,80,90,100]
print(list(sorted(list(set(li))))[-2])

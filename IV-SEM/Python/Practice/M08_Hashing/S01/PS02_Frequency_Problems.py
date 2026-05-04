'''
#Count Frequency of each element 
#[1, 2, 4, 3, 1, 2, 5] ==> {1:2, 2:2, 3:1, 4:1, 5:1}
li = list(map(int, input().split()))
d = {}
for el in li:
    if ele not in d:
        d[ele] = 1
    else:
        d[ele] += 1
print(d)

d1 = {}
for ele in li:
    d1[el] = d1.get(el, 0) + 1
print(d1)

from collections import Counter
print(Counter(li))

#find all distinct elements
#[1,2,4,3,1,2,5] ==> [1,2,3,4,5]

li = list(map(int, input().split()))
s = set()
for ele in li:
    if ele not in s:
        s.add(ele)
print(list(s))
'''
#Find the element with maximum frequency 
#[1,2,4,3,1,2,5,1] ==> 1
from collections import Counter 
li = list(map(int, input().split()))
freq = dict(Counter(li))
print(max(freq,key=freq.get))

#leetcode 169 Majority Element
#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times. You may assume that the majority element always exists in the array.
from collections import Counter 
li = list(map(int, input().split()))
freq = dict(Counter(li))
majority_element = max(freq, key=freq.get)
print(majority_element) 

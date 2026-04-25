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

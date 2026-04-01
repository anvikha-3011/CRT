'''
#input : [12, 45, 36, 78,96]
#output : [96, 78, 36, 45, 12]
li = [12, 45, 36, 78,96]
res = []
stop = -1 * (len(li) + 1)
for i in range(-1, stop, -1):
    res.append(li[i])
print(res)
#list comprehension
res1 = [li[i] for i in range(-1, stop, -1)]
print(res1)
'''
'''
#using swapping technique
li = [12, 45, 36, 78,96]
n = len(li)
print("Before reversing:", li)
for i in range(n//2):
    li[i], li[n-1-i] = li[n-1-i], li[i]
print("After reversing:", li)
'''
#using slicing technique
li = [12, 45, 36, 78,96]
res = []
for ele in li:
    #res.insert(0,ele)
    res = [ele] + res
print(res)